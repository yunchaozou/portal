"""
Django settings for jsclearing project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR,'jsclearing')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jcj+tdsh$=q4jbg3$^rg^m-(*jje)ve)1ayy%yfwphsz4qr_(^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
    'redactor',
    'jsclearing.poll',
    'jsclearing.notice',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'jsclearing.urls'

WSGI_APPLICATION = 'jsclearing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'jsclearing',
        'USER':'root',
        'PASSWORD':'1234',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia-Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR,'static').replace('\\'  , '/')
STATICFILES_DIRS = (

    # Put strings here, like "/home/html/static" or "C:/www/django/static".

    # Always use forward slashes, even on Windows.

    # Don't forget to use absolute paths, not relative paths.
     os.path.join(PROJECT_DIR,'static').replace('\\'  , '/'),
     
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    # Always use forward slashes, even on Windows.
    os.path.join(PROJECT_DIR,'templates').replace('\\'  , '/'),
    
)

MEDIA_ROOT =  os.path.join(BASE_DIR , 'media').replace('\\'  , '/')
MEDIA_URL =  '/media/'



#setting for wysiwsgeditor
REDACTOR_OPTIONS = {'lang': 'zh_cn'}
REDACTOR_UPLOAD = 'uploads/'