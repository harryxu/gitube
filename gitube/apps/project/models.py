import hashlib

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User, Group

from django.conf import settings
tblname = getattr(settings, 'TABLE_NAME_FORMAT', 'gitube_%s')

class Project(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    owner       = models.ForeignKey(User)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(max_length=255, unique=True)
    is_public   = models.BooleanField(default=0)

    class Meta:
        db_table = tblname % 'projects'

    def __unicode__(self):
        return self.name

    def canRead(self, user):
        if user == self.owner or self.is_public:
            return True
        try:
            ProjectUserRoles.objects.get(project=self, user=user)
            return True
        except ProjectUserRoles.DoesNotExist:
            return False

    def canPush(self, user):
        """Check if user can push code to project repos."""
        if user == self.owner or self.is_public:
            return True
        try:
            ProjectUserRoles.objects.get(
                Q(group=Group.objects.get(name='admin'))|Q(group=Group.objects.get(name='developer')),
                project=self, user=user)
            return True
        except ProjectUserRoles.DoesNotExist:
            return False

    def isAdmin(self, user):
        if user == self.owner:
            return True
        try:
            ProjectUserRoles.objects.get(
                project=self, user=user, group=Group.objects.get(name='admin'))
            return True
        except ProjectUserRoles.DoesNotExist:
            return False

    @models.permalink
    def get_absolute_url(self):
        return ('view_project', (), {
                    'pslug': str(self.slug)})

class Repository(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField()
    project     = models.ForeignKey(Project)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(max_length=255)
    path_hash   = models.CharField(max_length=64, unique=True)
    is_public   = models.BooleanField(default=0)

    class Meta:
        db_table = tblname % 'repositories'

    def save(self, *args, **kwargs):
        """docstring for save"""
        path = '%s/%s.git' % (self.project.slug, self.slug)
        self.path_hash = hashlib.sha1(path).hexdigest()
        super(Repository, self).save(*args, **kwargs)

    def canRead(self, user):
        if user == self.project.owner or self.is_public:
            return True
        try:
            RepositoryUserRoles.objects.get(repo=self, user=user)
            return True
        except RepositoryUserRoles.DoesNotExist:
            return self.project.canRead(user)

    def canPush(self, user):
        """docstring for canPush"""
        if user == self.project.owner or self.is_public:
            return True
        return self.project.canPush(user)

    def isAdmin(self, user):
        if user == self.project.owner:
            return True
        try:
            RepositoryUserRoles.objects.get(
                repo=self, user=user, group=Group.objects.get(name='admin'))
            return True
        except RepositoryUserRoles.DoesNotExist:
            return self.project.isAdmin(user)

    def __unicode__(self):
        return self.name

    def gitAddres(self):
        """docstring for gitAddres"""
        addr = '%(user)s@%(host)s:%(project)s/%(repo)s.git' % {
                        'user': getattr(settings, 'SSH_USER'),
                        'host': getattr(settings, 'GIT_HOST'),
                        'project':self.project.slug,
                        'repo':self.slug}
        return addr

    @models.permalink
    def get_absolute_url(self):
        return ('view_repo', (), {
                    'pslug': str(self.project.slug),
                    'rslug': str(self.slug)})


class RepositoryUserRoles(models.Model):
    user  = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    repo  = models.ForeignKey(Repository)

    class Meta:
        db_table = tblname % 'repository_user_roles'

class ProjectUserRoles(models.Model):
    user     = models.ForeignKey(User)
    group    = models.ForeignKey(Group)
    project  = models.ForeignKey(Project)

    class Meta:
        db_table = tblname % 'project_user_roles'
