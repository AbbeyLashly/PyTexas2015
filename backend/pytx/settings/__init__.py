"""
Django settings for pytx project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(
  os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
  )
)

DEBUG = False

ALLOWED_HOSTS = [
  'pytexas.org',
  '.pytexas.org',
]


# Application definition

INSTALLED_APPS = (
  'grappelli',
  
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  
  'django_markdown',
  'rest_framework',
  'imagekit',
  
  'twospaces.profiles',
  'twospaces.conference',
  'twospaces.blog',
  
  'pytx',
)

MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'twospaces.middleware.JsonRequest',
)

ROOT_URLCONF = 'pytx.urls'

FRONT_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'frontend')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [FRONT_ROOT],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pytx.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE':'django.db.backends.postgresql_psycopg2',
    'NAME': 'pytexasweb3',
    'USER': 'postgres',
    'HOST': 'db.internal',
    'PORT': '5432',
  }
}

SESSION_COOKIE_HTTPONLY = False

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_URL = '/static/'
STATIC_ROOT = '/home/www/PyTexasWeb/frontend/static/'

MEDIA_URL = '/static/uploads/'
MEDIA_ROOT = '/home/www/PyTexasWeb/frontend/static/uploads/'

AUTH_USER_MODEL = 'profiles.User'
GRAPPELLI_ADMIN_TITLE = 'PyTexas Admin'
SITE_NAME = 'PyTexas'

DEFAULT_CONF = '2015'

GRAVATAR_DEFAULT_IMAGE = 'retro'

DEFAULT_FROM_EMAIL = 'conference@pytexas.org'

TWOSPACES_SPEAKER_NOTIFY = ['conference@pytexas.org']
TWOSPACES_SPONSOR_NOTIFY = ['conference@pytexas.org']

EVENTBRITE_API_URL = 'https://www.eventbriteapi.com/v3'
EVENTBRITE_OAUTH_TOKEN = ''
EVENTBRITE_EVENT_ID = ''

WEEKLY_STATS_EMAIL = 'conference@pytexas.org'
WEEKLY_STATS_FROM_EMAIL = DEFAULT_FROM_EMAIL

from pytx.settings.local import *

