import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from chat.consumers import ChatConsumer
from django.urls import re_path

os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/chat/(?P<room_id>\w+)/$', ChatConsumer.as_asgi()),
        ])
    ),
})
