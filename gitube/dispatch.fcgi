#!/usr/bin/env python

import sys
import os

os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'

sys.path.append('/home/harry/workspaces/python/libs/django')
sys.path.append('/home/harry/workspaces/python/gitube')

os.environ['DJANGO_SETTINGS_MODULE'] = 'gitube.settings'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
