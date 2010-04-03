import hashlib

from gitube.apps.project.models import Project, Repository
from django.contrib.auth.models import User

def haveAccess(config, user, mode, path):
    """ Access controll """
    myuser = User.objects.get(username=user)
    if not myuser:
        return None

    pathHash = hashlib.sha1(path).hexdigest()
    repo = Repository.objects.get(path_hash=pathHash)

    if not repo:
        return None

    

    
