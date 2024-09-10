from django.urls import path
from . import consumers

websocket_urlspattens = [
    path("ws/sc/",consumers.MySyncConsumer.as_asgi()),
]