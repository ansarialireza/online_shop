"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i9tnv-&0kt%-ly_kw%ve!m=bx_50#6^g^y136a$_zmpy396+%x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.humanize',
    'django_extensions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'robots',
    'taggit',
    'django_summernote',
    'captcha',
    'compressor',
    'jalali_date',
    'mptt',
    'persian_tools',
    'azbankgateways',
    'payments',

    'website',
    'cart',
    'products',
    'orders',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'cart.middleware.CartMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTHENTICATION_BACKENDS = [
    'accounts.backends.CustomUserBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_USER_MODEL = 'accounts.User'
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tehran'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Additional static files directories
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#_______________________________________________________________

MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

X_FRAME_OPTIONS = "SAMEORIGIN"



COMPRESSOR_BACKEND = 'compressor.backends.htmlmin.HtmlMinCompressor'

# Enable or disable the compressor
COMPRESS_ENABLED = True
STATIC_DEPS=True
COMPRESS_URL = '/static/'
# Add the following settings if you want to use precompilers for CSS and JS
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
    ('text/javascript', 'babel --presets es2015,react {infile} -o {outfile}'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
    'compressor.finders.CompressorFinder',
)

# ROBOTS_USE_SITEMAP = True
# ROBOTS_SITEMAP_URLS = [
#     'http://www.ansrza.ir/sitemap.xml',
# ]

# settings.py


# default settings (optional)
JALALI_DATE_DEFAULTS = {
   'Strftime': {
        'date': '%y/%m/%d',
        'datetime': '%H:%M:%S _ %y/%m/%d',
    },
    'Static': {
        'js': [
            # loading datepicker
            'admin/js/django_jalali.min.js',
            # OR
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
            # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
            # 'admin/js/main.js',
        ],
        'css': {
            'all': [
                'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
            ]
        }
    },
}


AZ_IRANIAN_BANK_GATEWAYS = {
   'GATEWAYS': {
       'ZARINPAL': {
           'MERCHANT_CODE': '0dbb3d9d-41f7-4776-b97d-545e81377eda',
           'SANDBOX': 0,  # 0 disable, 1 active
       },
   },
   'IS_SAMPLE_FORM_ENABLE': True, # اختیاری و پیش فرض غیر فعال است
   'DEFAULT': 'ZARINPAL',
   'CURRENCY': 'IRT', # اختیاری
   'TRACKING_CODE_QUERY_PARAM': 'tc', # اختیاری
   'TRACKING_CODE_LENGTH': 16, # اختیاری
   'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader', # اختیاری
   'BANK_PRIORITIES': [
       'ZARINPAL',
       # and so on ...
   ], # اختیاری
   'IS_SAFE_GET_GATEWAY_PAYMENT': False, #اختیاری، بهتر است True بزارید.
   'CUSTOM_APP': None, # اختیاری 
}