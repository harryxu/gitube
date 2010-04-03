import hashlib

from gitube.apps.project.models import Project, Repository
from django.contrib.auth.models import User

from django.contrib.auth.models import settings

def haveAccess(config, user, mode, path):
    """ Access controll """
    myuser = User.objects.get(username=user)
    if not myuser:
        return None

    pathHash = hashlib.sha1(path).hexdigest()
    repo = Repository.objects.get(path_hash=pathHash)

    if not repo:
        return None

    if mode == 'read' and not repo.canRead(myuser):
        return None
    if mode == 'write' and not repo.isAdmin():
        return None

    prefix = getattr(settings, 'REPO_BASE_PATH', 'repositories')
    return (prefix, path)
