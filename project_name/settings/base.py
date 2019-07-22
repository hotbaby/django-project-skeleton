# encoding: utf8

import os
import sys

DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(DJANGO_ROOT)
SITE_NAME = os.path.basename(DJANGO_ROOT)
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'run', 'static')
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'run', 'media')

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

PROJECT_TEMPLATES = [
    os.path.join(PROJECT_ROOT, 'templates'),
]

# add apps/ to the Python path
sys.path.append(os.path.normpath(os.path.join(PROJECT_ROOT, 'apps')))


# ##### APPLICATION CONFIGURATION #########################

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'applications',
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# template stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

# ##### SECURITY CONFIGURATION ############################

# We store the secret key here
# The required SECRET_KEY is fetched at the end of this file
SECRET_FILE = os.path.normpath(os.path.join(PROJECT_ROOT, 'run', 'SECRET.key'))

ADMINS = (
    ('your name', 'your_name@example.com'),
)
MANAGERS = ADMINS


# ##### DJANGO RUNNING CONFIGURATION ######################

WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME
DATABASE_ROUTERS = ['{{ project_name }}.db_router.DatabaseRouter']

ROOT_URLCONF = '%s.urls' % SITE_NAME

# the URL for static files
STATIC_URL = '/static/'

# the URL for media files
MEDIA_URL = '/media/'


# ##### DEBUG CONFIGURATION ###############################
DEBUG = False

SECRET_KEY = '6x5m(zd6-l%wm21rxqkt8vky@taei5e+66lhnji5!a!eq5cstj'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'app': {
            'format': '%(asctime)s|%(levelname)s|%(process)d|%(module)s|%(funcName)s|%(lineno)d|%(message)s',
        },
        'access': {
            'format': '%(asctime)s|%(levelname)s|%(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'access': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'logs/access.log'),
            'formatter': 'access',
        },
        'app': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'logs/app.log'),
            'formatter': 'app'
        },
        'error': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.path.join(PROJECT_ROOT, 'logs/error.log'),
            'formatter': 'app',
            'level': 'ERROR',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        'access': {
            'handlers': ['access'],
            'level': os.getenv('HZF_ACCESS_LOG_LEVEL', 'INFO'),
        },
        'app': {
            'handlers': ['app', 'console', 'error'],
            'level': os.getenv('HZF_APP_LOG_LEVEL', 'INFO'),
        },
    },
}


LANGUAGE_CODE = 'en-us'

USE_TZ = False
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True
USE_L10N = True
