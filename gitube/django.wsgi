#!/usr/bin/env python

import os
import sys

os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE'] = 'gitube.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
