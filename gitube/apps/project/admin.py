from django.contrib import admin
from gitube.apps.project import models

admin.site.register(models.Project)
admin.site.register(models.Repository)
