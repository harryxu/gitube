from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
tblname = getattr(settings, 'TABLE_NAME_FORMAT', 'gitube_%s')

class SSHKey(models.Model):
    title = models.CharField(max_length=50)
    key   = models.TextField()
    user  = models.ForeignKey(User)

    class Meta:
        db_table = tblname % 'ssh_keys'

    def __unicode__(self):
        return self.title
