from pathlib import Path
from env_loader import load_env

# Load settings from .env
env = load_env(".envs/")


# Base Django settings

ROOT_DIR = Path(__file__).resolve().parent
BASE_DIR = ROOT_DIR.parent

ALLOWED_HOSTS = env.get("ALLOWED_HOSTS", [])
DEBUG = env.get("DEBUG", False)
SECRET_KEY = env.get("SECRET_KEY", None)


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

SHORTYURL_APPS = [
    "shortyurl.common",
    "shortyurl.urls",
]

INSTALLED_APPS = DJANGO_APPS + SHORTYURL_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "shortyurl.urlconf"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ROOT_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "shortyurl.wsgi.application"


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.get("POSTGRES_DB"),
        "USER": env.get("POSTGRES_USER"),
        "PASSWORD": env.get("POSTGRES_PASSWORD"),
        "HOST": env.get("POSTGRES_HOST"),
        "PORT": env.get("POSTGRES_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Project specific settings
ALIAS_MINIMUM_LENGTH = env.get("ALIAS_MINIMUM_LENGTH", 8)
ALIAS_GENERATION_MAX_RETRIES = env.get("ALIAS_GENERATION_MAX_RETRIES", 5)
REDIRECT_DOMAIN = env.get("REDIRECT_DOMAIN", "http://127.0.0.1:8000")
