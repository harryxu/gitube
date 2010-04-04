#!/usr/bin/env python

import os
import sys

os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'

sys.path.append('/home/harry/workspaces/python/libs/django')
sys.path.append('/home/harry/workspaces/python/gitube')

os.environ['DJANGO_SETTINGS_MODULE'] = 'gitube.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
