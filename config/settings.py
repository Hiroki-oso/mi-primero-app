from pathlib import Path
import os
from django.contrib import messages #メッセージ表示用で追記
from django.core.management.utils import get_random_secret_key # 追記
SECRET_KEY = get_random_secret_key() # 追記
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
DEBUG=False
ALLOWED_HOSTS=['127.0.0.1', 'herokuapp.com'] # 追記
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
    "whitenoise.middleware.WhiteNoiseMiddleware",
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
        "NAME": "name",
        "USER": "user",
        "PASSWORD": " ",
        "HOST": "host",
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
# カスタムユーザーモデル
AUTH_USER_MODEL = 'accounts.User'

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# ログイン、ログアウト
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/list/'
LOGOUT_URL = '/logout/'
LOGOUT_REDIRECT_URL = '/top/'
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.INFO: 'alert alert-info',
    messages.SUCCESS: 'alert alert-success',
}
#追記
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
# 追記
#Heroku database
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
db_from_env = dj_database_url.config(conn_max_age=600,
ssl_require=True)
DATABASES['default'].update(db_from_env)
try:
 from .local_settings import *
except ImportError:
 pass
if not DEBUG:
    SECRET_KEY = get_random_secret_key() #削除  

import django_heroku
django_heroku.settings(locals())