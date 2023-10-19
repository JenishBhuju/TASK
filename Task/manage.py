import os
import sys
import dotenv

def main():
    # Set DJANGO_SETTINGS_MODULE to your project's settings module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoauthapi1.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Load environment variables from .env file
    dotenv.load_dotenv()

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
