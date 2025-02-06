import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VPS_test_mini_project.settings')

application = get_asgi_application()
