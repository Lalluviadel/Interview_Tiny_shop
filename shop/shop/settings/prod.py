import os

from .base import *

SECRET_KEY = 'django-insecure-kepnjv5!9vr(mp&b6v11z!9^aw3ab!6)x--rz^pe0etnq+jn0s'
DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tinyshop',
        'USER': 'dns',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432',
    }
}
