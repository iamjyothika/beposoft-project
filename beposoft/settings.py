"""
Django settings for beposoft project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a0e4^&1w3e78i(lrlq*5$vvwt9ekdp&1r^4^$qjt050b(g$bs4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','*']


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
]


CORS_ALLOW_ALL_ORIGINS  = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-requested-with',
    'accept',
    'origin',
    'accept-encoding',
    'x-csrftoken',
]



SECURE_COOKIE = True

JWT_EXPIRATION_MINUTES = 1440 

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'beposoft_app',
    'bepocart',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'beposoft.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'beposoft.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {  
#     'default': {  
#         'ENGINE': 'django.db.backends.postgresql',  
#         'NAME': 'beposoft_db',  
#         'USER': 'postgres',  
#         'PASSWORD': 'bepoindia',  
#         'HOST': 'database-1.cje486w6gaav.ap-south-1.rds.amazonaws.com',  
#         'PORT': '5432', 
#     }  
# } 

DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.mysql',  
        'NAME': 'beposoft_db',  
        'USER': 'beposoft',  
        'PASSWORD': 'bepoindia',  
        'HOST': 'database-2.cje486w6gaav.ap-south-1.rds.amazonaws.com',  
        'PORT': '3306', 
    }  
}  



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'  
MEDIA_URL = '/media/'    
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  






# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
