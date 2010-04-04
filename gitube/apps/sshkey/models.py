import os
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

authorized_keys = '~%s/.ssh/authorized_keys' % getattr(settings, 'SSH_USER')
authorized_keys = os.path.expanduser(authorized_keys)

keysTobeRemove = []

def preSaveHandler(sender, instance, **kwargs):
    """docstring for preSaveHandler"""
    if instance.id is not None and instance.id > 0:
        oldKey = sender.objects.filter(pk=instance.pk).get().key
        keysTobeRemove.append(oldKey)

def pubkeySaveHandler(sender, instance, **kwargs):
    """docstring for pubkeySaveHandler"""
    username = instance.user.username
    newKey = instance.key
    ssh.writeKey(authorized_keys, username, newKey)

    for key in keysTobeRemove:
        ssh.removeKey(authorized_keys, username, key)
        keysTobeRemove.remove(key)


def pubkeyRemoveHandler(sender, instance, **kwargs):
    """docstring for pubkeyRemoveHandler"""
    if instance.id is not None and instance.id > 0:
        ssh.removeKey(authorized_keys, instance.user.username, instance.key)

pre_save.connect(preSaveHandler, sender=SSHKey)
post_save.connect(pubkeySaveHandler, sender=SSHKey)
post_delete.connect(pubkeyRemoveHandler, sender=SSHKey)
