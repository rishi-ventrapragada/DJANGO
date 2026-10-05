"""
WSGI config for shopping_cart project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_cart.settings')

application = get_wsgi_application()
