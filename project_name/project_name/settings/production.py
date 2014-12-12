from os import environ

from .base import *

from django.core.exceptions import ImproperlyConfigured


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_database',
        'USER': 'db_user',
        'PASSWORD': 'xxxxx',
        'HOST': 'xxxx.com',
        'PORT': '',
    }    
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

SECRET_KEY = get_env_setting('SECRET_KEY')

INSTALLED_APPS += (
    'gunicorn',
)
