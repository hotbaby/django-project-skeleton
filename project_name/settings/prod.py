# encoding: utf8

import os
from .base import *     # NOQA
from .base import DEFAULT_APPS, PROJECT_ROOT

DEBUG = False

ALLOWED_HOSTS = []

INSTALLED_APPS = DEFAULT_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'prod.sqlite3'),
    }
}
