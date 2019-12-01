"""
WSGI config for DrAdvisor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.shortcuts import render
from django.http import HttpResponse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DrAdvisor.settings')

application = get_wsgi_application()
