from django.db import models
from django.contrib.auth.models import User, Permission, Group

class Project(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    user_id     = models.ForeignKey(User)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(max_length=255, unique=True)

class Repository(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    project_id  = models.ForeignKey(Project)
    user_id     = models.ForeignKey(User)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    is_public   = models.BooleanField(default=0)

class Team(models.Model):
    name        = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    user_id     = models.ForeignKey(User)
    users       = models.ManyToManyField(User)
        
class RepositoryUserRoles(models.Model):
    repo_id  = models.ForeignKey(Repository)
    user_id  = models.ForeignKey(User)
    group_id = models.ForeignKey(Group)

