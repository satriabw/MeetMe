"""
Django settings for meetme project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from decouple import config
import dj_database_url
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
#
# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'mhv(0np=fstiu_ywam-q3c9ccali2s4dj)!l8#o!+ee(dldi6a'
#
# # # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
#
# #For LocalConfig
# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.sqlite3',
#     #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     # }
#     # 'default': {
#     #     'ENGINE':  'django.contrib.gis.db.backends.postgresql',
#     #     'NAME': 'd826vl33rpnh26',
#     #     'USER': 'djwsiilvpegbnu',
#     #     'PASSWORD': 'e125a03870791e35ff26cd316b20fc9c8196b892902a4edc74b154cca53e75bd',
#     #     'HOST': 'ec2-23-21-197-175.compute-1.amazonaws.com',
#     #     'PORT': '5432',
#     # }
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'meetme',
#         'USER': 'postgres',
#         'PASSWORD': 'asdf1234()',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
#
# }


ALLOWED_HOSTS = ['*']
#for heroku config
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'matchmaking.apps.MatchmakingConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meetme.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'meetme.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    ),
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=60),
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
#
# STATIC_URL = '/static/'
STATIC_ROOT = 'static'
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static'),
# )
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()
# DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'