import os

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
ENV = os.environ.get('DJANGO_ENV', 'dev')

DEBUG = os.environ.get('DJANGO_DEBUG') == 'true' or ENV == 'dev'
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (os.environ.get('DJANGO_ADMIN_NAME', 'Admin'), os.environ.get('DJANGO_ADMIN_EMAIL', 'root@localhost')),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'DJANGO_DB_ENGINE',
            'django.db.backends.sqlite3' if ENV == 'dev' else 'django.db.backends.mysql',
        ),
        'NAME': os.environ.get(
            'DJANGO_DB_NAME',
            '.harhacker.db' if ENV == 'dev' else 'harhacker',
        ),
        'USER': os.environ.get('DJANGO_DB_USER', ''),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', ''),
        'HOST': os.environ.get('DJANGO_DB_HOST', ''),
        'PORT': os.environ.get('DJANGO_DB_PORT', ''),
    }
}

TIME_ZONE = os.environ.get('DJANGO_TIME_ZONE', 'GMT')
LANGUAGE_CODE = os.environ.get('DJANGO_LANGUAGE_CODE', 'en-us')
SITE_ID = 1
USE_I18N = True
USE_L10N = True
# User-uploaded files
MEDIA_ROOT = os.environ.get('MEDIA_ROOT', '/var/lib/harhacker/media')
MEDIA_URL = '/media/'
# Static files
STATIC_ROOT = os.environ.get('STATIC_ROOT', '/var/lib/harhacker/static')
STATIC_URL = '/static/'
# Admin static content
ADMIN_MEDIA_PREFIX = '/static/admin/'
# Database fixtures
FIXTURE_DIRS = os.path.join(ROOT_PATH, 'fixtures')

STATICFILES_DIRS = (
    os.path.join(ROOT_PATH, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Secret key
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'secret')

APPEND_SLASH = False
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'

ELASTIC_SEARCH_HOST = os.environ.get('DJANGO_ELASTIC_SEARCH_HOST', 'localhost:9200').split()
ELASTIC_SEARCH_TIMEOUT = 10

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'harhacker.urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
