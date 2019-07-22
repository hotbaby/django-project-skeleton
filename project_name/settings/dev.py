# encoding: utf8

import os

from .base import *     # NOQA
from .base import DEFAULT_APPS, PROJECT_ROOT

DEBUG = True

ALLOWED_HOSTS = ['*']

LOGIN_URL = 'core_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'core_login'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'dev.sqlite3'),
    }
}

INSTALLED_APPS = DEFAULT_APPS
