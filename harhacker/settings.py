import os

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
ENV = os.environ.get('ENV', 'dev')

DEBUG = os.environ.get('DEBUG') == 'true' or ENV == 'dev'
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    (os.environ.get('ADMIN_NAME', 'Admin'), os.environ.get('ADMIN_EMAIL', 'root@localhost')),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'DB_ENGINE',
            'django.db.backends.sqlite3' if ENV == 'dev' else 'django.db.backends.mysql',
        ),
        'NAME': os.environ.get(
            'DB_NAME',
            '.harhacker.db' if ENV == 'dev' else 'harhacker',
        ),
        'USER': os.environ.get('DB_USER', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
    }
}

TIME_ZONE = os.environ.get('TIME_ZONE', 'GMT')
LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-us')
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
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')

APPEND_SLASH = False
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'

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
    'harhacker.dashboards',
    'harhacker.pollers',
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
