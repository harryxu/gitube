from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
tblname = getattr(settings, 'TABLE_NAME_FORMAT', 'gitube_%s')


# Create your models here.

class MemberList(models.Model):
    title = models.CharField(max_length=60)
    owner = models.ForeignKey(User)
    users = models.ManyToManyField(User, related_name='list_users')
    
    class Meta:
        db_table = tblname % 'member_list'
    