# Django Channels WebSocket Setup
## Overview
This README provides a step-by-step guide to setting up Django Channels with WebSocket support, enabling real-time communication in your Django application.

## Prerequisites
- Python 3.x
- Django 3.x or higher
## Basic knowledge of Django and Python
Installation
Install the necessary packages:


```
pip install daphne channels channels-redis
```
Django Channels Setup
1. Configure ASGI Application
In your Django project's settings file (settings.py), add the following:

### python
ASGI_APPLICATION = 'Jahangir.asgi.application'
2. Create asgi.py
Create an asgi.py file in your project directory:

### python

```
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import app.routing as r

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jahangir.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            r.websocket_urlpatterns
        )
    ),
})
```

# Define WebSocket Routing
In your app, create a routing.py file:
```
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/sc/", consumers.MySyncConsumer.as_asgi()),
]
```
# Create Consumers

from channels.consumer import SyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio

```
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Connected...", event)
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        print("Received by...", event)
        print(event['text'])
        self.send({
            "type": "websocket.send",
            "text": "Bhaia kemon achen?",
        })

    def websocket_disconnect(self, event):
        print("Disconnected...", event)
```

```
class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected...", event)
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        for i in range(50):
            await self.send({
                "type": "websocket.send",
                "text": str(i),
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print("Disconnected...", event)
```
# Frontend WebSocket Integration
** JavaScript WebSocket Client **
Add the following JavaScript code to your HTML to establish a WebSocket connection:
javascript

```
const ws = new WebSocket("ws://localhost:8000/ws/sc/");

ws.onopen = (event) => {
    console.log("WebSocket connection open...");
    ws.send("HI, Message from client...");
};

ws.onmessage = (event) => {
    console.log("Message received from server:", event.data);
    document.getElementById("test").innerHTML = event.data;
};
```
Channels Layer
Django Channels Layer allows communication between different instances of an application, facilitating distributed real-time applications.

Redis Channels Layer
To use Redis as your channels layer, you need to configure it in your settings:

Install the Redis package:

```pip install channels-redis```
Add the following to your settings:

# When Use of reids sever 
```
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
```
# When Use of In momory location 
```
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

```
# Always this Middleware
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

# Summary
You now have a basic setup for using Django Channels with WebSocket support. This allows for real-time communication between the server and clients. You can further extend this by implementing additional features like user authentication, group messaging, and more.

# Note
Make sure to run a Redis server locally or in your production environment to utilize the Channels Layer effectively.

For more detailed information, check the official Django Channels documentation.
