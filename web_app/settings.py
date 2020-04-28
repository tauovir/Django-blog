"""
Django settings for web_app project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8e0p!a4zm6nceupilti_&-+c*x722zkczvxjza0nih*i9&s1%u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #own registry
    'ckeditor',
    'ckeditor_uploader',
    'blog',
    'clear_cache',
    # All auth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Required service provoider
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

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

ROOT_URLCONF = 'web_app.urls'

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
                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'web_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'blog_app',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : '',
        'PORT' : '',
        'OPTION' : {
            'init_command' : "SET sql_mode = 'STRICT_TRANS_TABLES'"
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR,'blog/static/assets/images/blog/') # Path where we want to store outr filr
MEDIA_ROOT = os.path.join(BASE_DIR,'media/') # Path where we want to store outr filr

#=============Email Setting============
SENDGRID_API_KEY = 'xyz'
EMAIL_HOST = 'xyz'
EMAIL_HOST_USER =  'xyz' #'Your Sendgrid user'
EMAIL_HOST_PASSWORD =  'xyz' #'yOUR sENDGRID PASSW
EMAIL_PORT= 587
EMAIL_USE_TLS = True
DEFAULT_TO_EMAIL = 'taukir707@gmail.com'
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Contact Emial receieved from Blog"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
############################### CKEDITOR CONFIGURATION ###################
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js' #refers to the jquery file which CKEditor uses.
CKEDITOR_UPLOAD_PATH = 'ckuploads/' # refers the directory where images will be uploaded relative to your MEDIA_ROOT.
CKEDITOR_IMAGE_BACKEND = "pillow" # refers to the image library which CKEditor uses to create thumbnails to display in CKEditor gallery.
CKEDITOR_CONFIGS = { # refer to the settings which CKEditor uses to customize its appearance and behavior.
    'default': {
        'toolbar': None,
    },
}
###################################

#=============All Auth Setting=================
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
SITE_ID = 1
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
LOGIN_REDIRECT_URL = '/comment-redirect'
