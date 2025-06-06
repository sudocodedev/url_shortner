from pathlib import Path
import environ
import os

# General
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-@hw*0uj&21&_c+f58(d1u51jx_66g8j5ofxa1#t%d585*a2$&f"
DEBUG = True
ALLOWED_HOSTS = []


# Environment
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))


# Applications
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
THIRD_PARTY_APPS = []
CUSTOM_APPS = []
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CUSTOM_APPS


# Middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "src.urls"


# Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "src.wsgi.application"


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("DATABASE_DB", default=""),
        "USER": env.str("DATABASE_USER", default=""),
        "PASSWORD": env.str("DATABASE_PASSWORD", default=""),
        "HOST": env.str("DATABASE_HOST", default=""),
        "PORT": env.str("DATABASE_PORT", default=""),
    }
}


# Password validation
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


# Timezone & Localization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = False


# Static files
STATIC_URL = "static/"


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
