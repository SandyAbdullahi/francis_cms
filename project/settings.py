"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '+cchje#-=uxq63wyt$-1^dm^e++(x-ri0azo@^y&vbi)&r=2c7'

import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'


# redirect http to https 
# SECURE_HSTS_SECONDS = os.environ.get('DJANGO_DEBUG', '') != 'False'
# SECURE_SSL_REDIRECT = os.environ.get('DJANGO_DEBUG', '') != 'False'
# SECURE_HSTS_PRELOAD = os.environ.get('DJANGO_DEBUG', '') != 'False'

# SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get('DJANGO_DEBUG', '') != 'False'
# SESSION_COOKIE_SECURE = os.environ.get('DJANGO_DEBUG', '') != 'False'
# CSRF_COOKIE_SECURE = os.environ.get('DJANGO_DEBUG', '') != 'False'





ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # Apps
    # 'overextends',
    'home',
    'about',
    'services',
    'contact',
    'wagtail_hooks',


    #sass compressor
    'compressor',

    # Wagtail data transfer
    'wagtail_transfer',

    # WAGTAIL
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.styleguide',

    'modelcluster',
    'taggit',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'francis',
#         'USERNAME': 'ab',
#         'PASSWORD': 'ab'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_TZ = True

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True



import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# The absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, '/static/')

# The URL to use when referring to static files (where they will be served from)
STATIC_URL = 'static/'

STATICFILES_FINDERS = [
    'compressor.finders.CompressorFinder'
]

COMPRESS_ROOT = 'static'

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Media settings for wagtail and deployment
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'




# WAGTAIL SITE NAME
WAGTAIL_SITE_NAME = 'Francis Interior Design'

WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = True



WAGTAILTRANSFER_SOURCES = {
    'staging': {
        'BASE_URL': 'http://localhost:3000/wagtail-transfer/',
        'SECRET_KEY': '4ac4822149691395773b2a8942e1a472',
    },
    'production': {
        'BASE_URL': 'https://francisinteriordesigns.pythonanywhere.com/wagtail-transfer/',
        'SECRET_KEY': 'a36476ffc6af34dc935570d97369eca0',
    },
}

WAGTAILTRANSFER_SECRET_KEY = '7cd5de8229be75e1e0c2af8abc2ada7e'