from django.db import models
from django.contrib.auth.models import User

from gitube.settings import TABLE_FORMAT

class SSHKey(models.Model):
    key     = models.TextField()
    title   = models.CharField(max_length=50)
    user    = models.ForeignKey(User)

    class Meta:
        db_table = TABLE_FORMAT % 'ssh_keys'
