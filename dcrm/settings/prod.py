from .base import *
import environ
import os

# Initialize environment variables
env = environ.Env()

# Determine which .env file to read
env_file = os.getenv('DJANGO_ENV_FILE', '.env')
env.read_env(os.path.join(BASE_DIR, env_file))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

SECURE_HSTS_SECONDS= env("SECURE_HSTS_SECONDS")
SECURE_SSL_REDIRECT= env("SECURE_SSL_REDIRECT")
SESSION_COOKIE_SECURE= env("SESSION_COOKIE_SECURE")
SECURE_HSTS_INCLUDE_SUBDOMAINS= env("SECURE_HSTS_INCLUDE_SUBDOMAINS")
CSRF_COOKIE_SECURE= env("CSRF_COOKIE_SECURE")
SECURE_HSTS_PRELOAD= env("SECURE_HSTS_PRELOAD")
WSGI_APPLICATION= env("WSGI_APPLICATION")

# Whitenoise settings
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  # Add after SecurityMiddleware

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

SECRET_KEY = env("SECRET_KEY")

DEBUG=False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": "5432",
    }
}