from gitube.forms import BaseModelForm
from gitube.apps.sshkey import models

class KeyForm(BaseModelForm):
    class Meta:
        model = models.SSHKey
        fields = ('title', 'key')
    
