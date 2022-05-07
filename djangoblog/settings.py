"""
Django settings for djangoblog project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta #auto logout
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-f*veq048om8bzlry#6(2sdo6bfjb8smi=lih62se4our0!5j1o'

ALLOWED_HOSTS = ['.herokuapp.com','127.0.0.1'] #to read by nginx

# Application definition

INSTALLED_APPS = [
    'channels',
    #'adminlte3',
    #'adminlte3_theme',
    'django.contrib.admin',
    #'django.contrib.auth',
    'setting.apps.AuthConfig',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic', #For Development Use
    'import_export',
    'tinymce',
    'debug_toolbar',
    'base',
    #'base.apps.BaseConfig', #base
    'setting.apps.SettingConfig', #setting app
    'blogpost', #blogpost app
    'chat',
    'register'
    #'admin_reorder'

]

ASGI_APPLICATION = 'djangoblog.asgi.application'
WSGI_APPLICATION = 'djangoblog.wsgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer" #good for testing only 
    }
}

MIDDLEWARE = [
    #'admin_reorder.middleware.ModelAdminReorder',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout',
    'whitenoise.middleware.WhiteNoiseMiddleware' #whitenoice
   
]
"""
ADMIN_REORDER = (
    'base',
    'setting',
    { 'app':'blogpost','models':('blogpost.Post','blogpost.Category','blogpost.Tag')},
)
"""
#Auto Logout
#AUTO_LOGOUT = {'IDLE_TIME': 600}
AUTO_LOGOUT = {'IDLE_TIME': timedelta(minutes=20)} #logut after 20 minutes of idle

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

DEBUG = True

ROOT_URLCONF = 'djangoblog.urls'
#files url settings
STATIC_URL = '/staticflies/'
MEDIA_URL = '/uploaded_files/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles/bootstrap_album') #register manually other created directory for static files
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles") #set Where to copy the static files 
#MEDIA_ROOT = os.path.join(BASE_DIR, "uploaded_files")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage" #whitenoice

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates' #main templates directory
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', #To access media files {{MEDIA_URL}}
                'setting.context_processors.site_setting' #setting app context processor
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'djangoblog',
        'USER': 'django',
        'PASSWORD': 'Iamdjangouser23',
        'HOST': 'localhost',
        'PORT': '3306'
    }

}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/var/tmp/django_cache',
    }
}
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

IMPORT_EXPORT_USE_TRANSACTIONS = True


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
