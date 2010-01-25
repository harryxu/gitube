from django.db import models
from django.contrib.auth.models import User, Group

from gitube.settings import TABLE_FORMAT


class Project(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    owner       = models.ForeignKey(User)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(max_length=255, unique=True)

    class Meta:
        db_table = TABLE_FORMAT % 'projects'

class Repository(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    project     = models.ForeignKey(Project)
    owner       = models.ForeignKey(User)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    is_public   = models.BooleanField(default=0)

    class Meta:
        db_table = TABLE_FORMAT % 'repositories'

    def canRead(self, user):
        if user == self.owner or self.is_public:
            return True
        
        try:
            RepositoryUserRoles.objects.get(repo=self, user=user)
            return True
        except RepositoryUserRoles.DoesNotExist:
            repoTeamSubQuery = '`team_id` IN (SELECT DISTINCT `team_id` '\
                'FROM `%s` WHERE repo_id=%d)'\
                % (RepositoryTeamRoles._meta.db_table, self.id)
                
            t = Team.objects.distinct().filter(users=user)\
                            .extra(where=[repoTeamSubQuery])
                            
            return len(t) > 0

    def isAdmin(self, user):
        if user == self.owner:
            return True

        adminGroup = Group.objects.get(name='admin')
        try:
            RepositoryUserRoles.objects.get(repo=self, user=user, group=adminGroup)
            return True
        except RepositoryUserRoles.DoesNotExist:
            repoTeamSubQuery = '`team_id` IN (SELECT DISTINCT `team_id` '\
                'FROM `%s` WHERE repo_id=%d and group_id=%d)'\
                 % (RepositoryTeamRoles._meta.db_table, self.id, adminGroup.id)
                 
            t = Team.objects.distinct().filter(users=user)\
                            .extra(where=[repoTeamSubQuery])
                            
            return len(t) > 0

class Team(models.Model):
    name   = models.CharField(max_length=255, unique=True)
    owner  = models.ForeignKey(User, related_name='team_owner')
    users  = models.ManyToManyField(User)

    class Meta:
        db_table = TABLE_FORMAT % 'teams'

class RepositoryTeamRoles(models.Model):
    team  = models.ForeignKey(Team)
    group = models.ForeignKey(Group)
    repo  = models.ForeignKey(Repository)

    class Meta:
        db_table = TABLE_FORMAT % 'repository_team_roles'

class RepositoryUserRoles(models.Model):
    user  = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    repo  = models.ForeignKey(Repository)

    class Meta:
        db_table = TABLE_FORMAT % 'repository_user_roles'

