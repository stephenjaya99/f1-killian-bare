import os

import django_heroku

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# --Environment-----------------------------------------------------
DEBUG = os.getenv('DEBUG') != 'False'
IS_RUN_IN_PROD_ENV = os.getenv('DJANGO_ENV') == 'production'
# -------------------------------------------------------------------

# --Secret Key definition--------------------------------------------
SECRET_KEY = os.environ['SECRET_KEY']
# -------------------------------------------------------------------

# --Application definition-------------------------------------------
PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
]

ADDITIONAL_APPS = [
    'test_without_migrations',
    'rest_framework',
    'django_rq',
    'debug_toolbar',
    'corsheaders',
]

PROJECT_APPS = [
    'killian',
    'killian.apps.log',
    'killian.apps.example',
]

INSTALLED_APPS = PREREQ_APPS + ADDITIONAL_APPS + PROJECT_APPS
# -------------------------------------------------------------------

# --Django Settings--------------------------------------------------
SESSION_COOKIE_NAME = 'killiansessionid'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'

ALLOWED_HOSTS = []

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

django_heroku.settings(locals(), test_runner=False)
# -------------------------------------------------------------------

# --Caches-----------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        # If you're on Heroku
        'LOCATION': os.getenv('REDISCLOUD_URL', 'redis://localhost:6379'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'DB': 0,
            'DEFAULT_TIMEOUT': 3600,
        },
    },
}
# -------------------------------------------------------------------

# --RQ---------------------------------------------------------------
RQ_QUEUES = {
    'default': {
        'USE_REDIS_CACHE': 'default',
    },
    'high': {
        'USE_REDIS_CACHE': 'default',
    }
}
RQ_SHOW_ADMIN_LINK = True
# -------------------------------------------------------------------

# --Rest Framework Settings------------------------------------------
REST_FRAMEWORK = {
    'CHARSET': 'utf-8',
    'DEFAULT_PERMISSION_CLASSES': [],
    'DEFAULT_RENDERER_CLASSES': [
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'rest_framework.parsers.FormParser',
    ],
}
# -------------------------------------------------------------------

# --CORS Settings----------------------------------------------------
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_ALLOW_ALL = True # it can't be used together with CORS_ALLOW_CREDENTIALS
CORS_ORIGIN_WHITELIST = (
    'http://aru.local:5000',
    'http://localhost:3005',
    'http://localhost:5000',
    'http://localhost',
    'https://f1-loki.herokuapp.com.global.prod.fastly.net',
    'https://f1-loki.herokuapp.com',
    'https://dekoruma.com',
    'https://www.dekoruma.com',
    'https://dekoruma.global.ssl.fastly.net',
    'https://admin.dekoruma.com',
    'https://merchant.dekoruma.com',
    'https://tracking.dekoruma.com',
)
CORS_ALLOW_HEADERS = (
    'api-key',
    'user-auth-token',
    'partner-api-key',
    'x-requested-with',
    'x-hub-signature',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken',
    'user-agent',
    'accept-encoding',
    'session-id'
)
# -------------------------------------------------------------------

# --Email Related Settings-------------------------------------------
EMAIL_SUBJECT_PREFIX = '[Dekoruma] '
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SYSTEM_FROM_EMAIL = 'hello@dekoruma.com'
# -------------------------------------------------------------------

# --Logging Settings-------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'root': {
        'level': 'INFO',
        'handlers': ['console', ],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s > %(module)s -- %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    }
}
# -------------------------------------------------------------------
