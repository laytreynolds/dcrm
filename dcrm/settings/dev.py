from .base import *
import environ
import os
from pathlib import Path
# Initialize environment variables
env = environ.Env()
# Determine which .env file to read
env_file = os.getenv('DJANGO_ENV_FILE', '.env.dev')
env.read_env(os.path.join(BASE_DIR, env_file))
ALLOWED_HOSTS = ["*"]
SECRET_KEY = env("SECRET_KEY")

DEBUG=True

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": "d1aapbmgg8tt6a",
        "USER": "ucjidogioe523j",
        "PASSWORD": "pb1e84bd4d8062f9c27cb9eeb372a2a305aa8400bc9379d4648754b1716de4d8f",
        "HOST": "cfs632mn9c82a7.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com",
        "PORT": "5432",
    }
}