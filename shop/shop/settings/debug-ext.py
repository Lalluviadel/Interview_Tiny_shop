from shop.settings.debug import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tinyshop',
        'USER': 'dns',
        'PASSWORD': 'qwerty',
        'HOST': '127.0.0.1',
        'PORT': '54325',
    }
}
