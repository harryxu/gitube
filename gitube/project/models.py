from django.db import models
from django.contrib.auth.models import User, Permission, Group

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

class Team(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    owner       = models.ForeignKey(User, related_name='team_owner')
    users       = models.ManyToManyField(User)

    class Meta:
        db_table = TABLE_FORMAT % 'teams'
        
class RepositoryUserRoles(models.Model):
    repo  = models.ForeignKey(Repository)
    user  = models.ForeignKey(User)
    group = models.ForeignKey(Group)

    class Meta:
        db_table = TABLE_FORMAT % 'repository_user_roles'

