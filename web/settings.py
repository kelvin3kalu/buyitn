import os
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# ===============================
# SECURITY
# ===============================

# ❌ REMOVE fallback – Render MUST provide this
SECRET_KEY = os.environ["SECRET_KEY"]

# ❌ Do NOT read DEBUG from env on Render
DEBUG = False

# ===============================
# HOSTS & CSRF
# ===============================

ALLOWED_HOSTS = [
    "buyitn.onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://buyitn.onrender.com",
]

# ===============================
# APPLICATION
# ===============================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
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
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'web.wsgi.application'

# ===============================
# DATABASE
# ===============================

import dj_database_url

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.environ.get("DB_NAME", "buyit_db_fcza"),
        "USER": os.environ.get("DB_USER", "buyitn_user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "YourPasswordHere"),
        "HOST": os.environ.get("DB_HOST", "dpg-d54rbamuk2gs73bhs3cg-a"),
        "PORT": os.environ.get("DB_PORT", "5432"),
        "OPTIONS": {
            "sslmode": "require",       
        },
    }
}


# ===============================
# INTERNATIONALIZATION
# ===============================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ===============================
# STATIC FILES
# ===============================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ===============================
# DEFAULT PK
# ===============================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
