from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete
from django.contrib.auth.models import User

from django.conf import settings
tblname = getattr(settings, 'TABLE_NAME_FORMAT', 'gitube_%s')


class SSHKey(models.Model):
    title = models.CharField(max_length=50)
    key   = models.TextField()
    user  = models.ForeignKey(User)

    class Meta:
        db_table = tblname % 'ssh_keys'
        ordering = ['title']

    def __unicode__(self):
        return self.title


from gitube.tools import ssh

authorized_keys = '/home/%s/.ssh/authorized_keys' % getattr(settings, 'SYSTEM_USER')

def pubkeySaveHandler(sender, instance, **kwargs):
    """docstring for pubkeySaveHandler"""
    ssh.writeKey(authorized_keys, instance.user.username, instance.key)

def pubkeyRemoveHandler(sender, instance, **kwargs):
    """docstring for pubkeyRemoveHandler"""
    if instance.id is not None and instance.id > 0:
        ssh.removeKey(authorized_keys, instance.user.username, instance.key)

pre_save.connect(pubkeyRemoveHandler, sender=SSHKey)
post_save.connect(pubkeySaveHandler, sender=SSHKey)
post_delete.connect(pubkeyRemoveHandler, sender=SSHKey)
