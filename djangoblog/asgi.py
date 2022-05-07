"""
ASGI config for djangoblog project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from channels.auth import AuthMiddlewareStack

from channels.security.websocket import AllowedHostsOriginValidator

import chat.websocket_routing as routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoblog.settings')

application = ProtocolTypeRouter({
        'http':get_asgi_application(),
        'websocket': AllowedHostsOriginValidator( #ALLOWED_HOSTS/Origin in settings.py SECURITY PURPOSES
            AuthMiddlewareStack(
                URLRouter(
                    routing.websocket_urlpatterns
                )
            )
        )
    })
