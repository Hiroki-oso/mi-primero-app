from pathlib import Path
import os
import environ

from django.contrib import messages 
from django.core.management.utils import get_random_secret_key 
SECRET_KEY = get_random_secret_key() 
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
DEBUG=False
ALLOWED_HOSTS=['108.61.223.96' ,'local.host'] 
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts",
    "lifemanage",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATE_DIR,],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "config.wsgi.application"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "myproject",
        "USER": "myprojectuser",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": " ",
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
LANGUAGE_CODE = "ja"
TIME_ZONE = "Asia/Tokyo"
USE_I18N = True
USE_TZ = True
# ?????????????????????????????????
AUTH_USER_MODEL = 'accounts.User'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),
# )
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# ??????????????????????????????
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/list/'
LOGOUT_URL = '/logout/'
LOGOUT_REDIRECT_URL = '/'
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.INFO: 'alert alert-info',
    messages.SUCCESS: 'alert alert-success',
}
# MEDIA_URL = '/media/'
#??????????????????
# DEBUG=False
# try:
#     from .local_settings import *
# except ImportError:
#     pass

# if DEBUG:
#     ALLOWED_HOSTS = ['*']
#     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# else:
#     import environ
#     env = environ.Env()
#     env.read_env(os.path.join(BASE_DIR, '.env'))
     
#     SECRET_KEY = env('SECRET_KEY')
#     ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')
     
#     STATIC_ROOT = '/usr/share/nginx/html/static'
#     MEDIA_ROOT = '/usr/share/nginx/html/media'
     