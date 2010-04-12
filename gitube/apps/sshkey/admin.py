from django.contrib import admin
from gitube.apps.sshkey import models

admin.site.register(models.SSHKey)
