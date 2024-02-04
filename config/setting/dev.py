from config.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o-k&e=42c8kvzz+58m96on3-u!ea-x7v*yv*na3e!o^r@po-6)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',"localhost",]

#INSTALLED_APPS = []
TIME_ZONE = 'Asia/Tehran'

# sites framework
SITE_ID =2

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


X_FRAME_OPTIONS = 'SAMEORIGIN'


# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = BASE_DIR / "sent_emails"


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.ansrza.ir'
EMAIL_PORT = 465  # SMTP Port for SSL
EMAIL_USE_SSL = True  # Use SSL for secure connection
EMAIL_HOST_USER = 'alireza@ansrza.ir'
EMAIL_HOST_PASSWORD = 'UppT8hcM6NfVyEH'
DEFAULT_FROM_EMAIL = 'alireza@ansrza.ir'

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = None  # "None" means no strict SameSite policy
