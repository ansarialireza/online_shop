from config.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o-k&e=42c8kvzz+58m96on3-u!ea-x7v*yv*na3e!o^r@po-6)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.ansrza.ir','ansrza.ir']

#INSTALLED_APPS = []


# sites framework
SITE_ID = 2


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ansrzair_CV',
        'USER': 'ansrzair_CV',
        'PASSWORD': 'Ansari1999',
        'HOST': 'localhost',
        'PORT': '3306',
    }
 }


STATIC_ROOT = '/home/ansrzair/public_html/static'
MEDIA_ROOT = '/home/ansrzair/public_html/media'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

SECURE_BROWSER_XSS_FILTER = True
CSRF_COOKIE_SECURE =True
X_FRAME_OPTIONS = 'SAMEORIGIN'
SECURE_CONTENT_TYPE_NOSNIFF = True

## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'