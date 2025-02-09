from .base import *
import environ
import os
from pathlib import Path
# Initialize environment variables
env = environ.Env(
    DEBUG=(bool, False)
)
# Determine which .env file to read
env_file = os.getenv('DJANGO_ENV_FILE', '.env.dev')
env.read_env(os.path.join(BASE_DIR, env_file))
ALLOWED_HOSTS = ["*"]
SECRET_KEY = env("SECRET_KEY")
DEBUG="True"
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": "dcrm",
        "USER": "postgres",
        "PASSWORD": "Xok87187",
        "HOST": "localhost",
        "PORT": "5432",
    }
}