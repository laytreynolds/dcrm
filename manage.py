#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import environ

# Add the path to the dcrm directory
sys.path.append(os.path.abspath("dcrm.dcrm"))

# Load the appropriate .env file
env = environ.Env()
env_file = os.getenv("DJANGO_ENV_FILE", ".env.dev")
environ.Env.read_env(env_file)


def main():
    """Run administrative tasks."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "dcrm.dcrm.settings.dev"
    )  # Default to development settings

    settings_module = os.getenv("DJANGO_SETTINGS_MODULE", "dcrm.dcrm.settings.dev")
    os.environ["DJANGO_SETTINGS_MODULE"] = settings_module
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
