import os
import hashlib
import logging

from django.conf import settings
from gitube import settings as localSettings

settings.configure(DATABASES=localSettings.DATABASES)

from django.contrib.auth.models import User
from gitube.apps.project.models import Repository


#LOG_FILE = '/tmp/gitube/log'
#logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)

def haveAccess(config, user, mode, path):
    """ Access controll """
    logging.debug('check access for %(user)r as %(mode)r on %(path)r'
                    % {'user':user, 'mode':mode, 'path':path})

    try:
        myuser = User.objects.get(username=user)
    except User.DoesNotExist:
        logging.debug('User "%(user)r" not found' % {'user':user})
        return None

    basename, ext = os.path.splitext(path)
    if ext == '.git':
        path = basename

    pathHash = hashlib.sha1(path).hexdigest()
    try:
        repo = Repository.objects.get(path_hash=pathHash)
    except Repository.DoesNotExist:
        logging.debug('Repo %(path)r not found, hashed: %(hashed)r'
                % {'path':path, 'hashed':pathHash})
        return None
    
    if mode != 'readonly' and mode != 'writable':
        return None
    if mode == 'readonly' and not repo.canRead(myuser):
        return None
    elif mode == 'writable' and not repo.canPush(myuser):
        return None

    basename, ext = os.path.splitext(path)
    if ext == '.git':
        path = basename

    prefix = getattr(settings, 'REPO_BASE_PATH', 'repositories')
    return (prefix, path)
