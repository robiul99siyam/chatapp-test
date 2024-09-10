from channels.consumer import SyncConsumer,AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync


class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Connected...", event)
        async_to_sync(self.channel_layer.group_add)("programers", self.channel_name)
        self.send({
            "type": "websocket.accept",
        })

    def websocket_receive(self, event):
        print("Received by...", event)

        async_to_sync(self.channel_layer.group_send)(
            "programers",
            {
                "type": "chat.message",
                "message": event['text'],
            }
        )

    def chat_message(self, event):
        self.send({
            "type": "websocket.send",
            "text": json.dumps({
                "text": event['message']
            }),
        })  


    def websocket_disconnect(self, event):
        print("Disconnected...", event)
        async_to_sync(self.channel_layer.group_discard)("programers", self.channel_name)

class MyAsncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("Connected...",event)
        await self.send({
            "type": "websocket.accept",        
        })
        
    async def websocket_receive(self,event):
        for i in range(50):
            await self.send({
            "type":"websocket.send",
            "text":str(i),
            })
            await asyncio.sleep(1)
        


    async def websocket_disconnect(self, event):
        print("Disconnected...",event)


class MyAsyncConsumers(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notification", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notification", self.channel_name)

    async def chat_message(self, event):
        message = event['message']
        print(message)
        await self.send(text_data=json.dumps({
            'message': message
        }))
