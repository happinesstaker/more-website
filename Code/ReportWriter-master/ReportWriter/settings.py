# @OPENSOURCE_HEADER_START@
# MORE Tool
# Copyright 2016 Carnegie Mellon University.
# All Rights Reserved.
#
# THIS SOFTWARE IS PROVIDED "AS IS," WITH NO WARRANTIES WHATSOEVER.
# CARNEGIE MELLON UNIVERSITY EXPRESSLY DISCLAIMS TO THE FULLEST EXTENT
# PERMITTEDBY LAW ALL EXPRESS, IMPLIED, AND STATUTORY WARRANTIES,
# INCLUDING, WITHOUT LIMITATION, THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT OF PROPRIETARY
# RIGHTS.
#
# Released under a modified BSD license, please see license.txt for full
# terms. DM-0003473
# @OPENSOURCE_HEADER_END@
"""
Django settings for ReportWriter project.
Generated by 'django-admin startproject' using Django 1.8.2.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3z8b9g&(36(t@h5n4qge6un)@li)8w!8(k8vf9kq74k+r)+75u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Application definition

SITE_TITLE = 'Report Writer'
SENDER_EMAIL = 'Report Writer'

INSTALLED_APPS = (
    'base',
    'report',
    'invitation',
    'register',
    'admin_lte',
    'rest_api',
    'solo',
    'django_admin_bootstrapped',
    'autocomplete_light',
    'captcha',
    'frontpage',
    'widget_tweaks',
    'crispy_forms',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'register_approval',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'report_mailer',
    'user_profile',
    'mailer',
)

# Email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '18732.test.websec'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = '4)-!n;8ciD:Y9>'


# START: allauth settings
LOGIN_REDIRECT_URL = '/app/'
ACCOUNT_FORMS = {'signup': 'register.forms.CustomSignupForm',
                 'login': 'register.forms.CaptchaLoginForm',
                 }
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'
# END

# START: register settings
ACCOUNT_EXTRA_PRE_LOGIN_STEPS = ['invitation.utils.verify_email_if_invited',
                                 'register_approval.utils.check_admin_approval']
# END

# START: Capcha settings
RECAPTCHA_PUBLIC_KEY = '6LcQ5RsUAAAAADt3lPJThyLWPK1hd6ja9kiDVFfb'
RECAPTCHA_PRIVATE_KEY = '6LcQ5RsUAAAAACfW2F1qpmrYm_4mrIB1d37gtY_p'
NOCAPTCHA = True
RECAPTCHA_USE_SSL = True
# END


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'ReportWriter.middleware.WhodidMiddleware',
)

ROOT_URLCONF = 'ReportWriter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'allauth.account.context_processors.account',
            ],
        },
    },
]

from django.contrib import messages
MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error',
            messages.INFO: 'alert-success success',
}


WSGI_APPLICATION = 'ReportWriter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'reportwriter',
        'USER': 'maggie',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
# Enable Connection Pooling
# DATABASES['default']['ENGINE'] = 'django_postgrespool'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1
