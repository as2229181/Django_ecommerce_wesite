"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 3.2.18.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ndjd5wzavv%4w1pcr-)i0s$^rmf+^d(a*s@5245_sg7rb@$@!r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'widget_tweaks',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store.apps.StoreConfig',
    'taggit',
    'ckeditor',
    'ckeditor_uploader',
    'paypal.standard.ipn',


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

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'store.context_processor.default',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_ecommerce',
        'USER' : 'root',
        'PASSWORD' : '12345678',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'OPTIONS': {'ssl': False},
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')
    ]
MEDIA_URL='/images/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static/images')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


JAZZMIN_SETTINGS ={
    "site_header": "shopping",
    "site_brand": "e-commerce",
    "welcome_sign": "Welcome to the shop-backend",
      "copyright": "G-shin",




}
AUTH_USER_MODEL='store.User'



CKEDITOR_UPLOAD_PATH='uploads/'


CKEDITOR_CONFIGS={
    'default':{
        'skin':'moono',
        'codeSnippet_theme':'monokai',
        'toolbar':'all',
        'extraPlugins':','.join(
            [
                'codesnippet',
                'widget',
                'dialog'
            ]
        )
    }
}

'''
Django looger
'''


LOGGING={
    'version':1,
    'loggers'  :{
        'django':{
            'hanndlers':['file'],
            'level':'DEBUG'
        }
    },
    'handlers':{
        'file':{
            'level':'DEBUG',
            'class':'logging.FileHandler',
            'filename':'log.log'
        }
    },
    'formatters':{
        'formar_demo':{
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {mseeage}',
            'style': '{',
        }

    }
}


LOGIN_URL='login'

PAYPAL_RECEIVER_EMAIL ='sb-nc43jj25477739@business.example.com'
PAYPAL_TEST = True
