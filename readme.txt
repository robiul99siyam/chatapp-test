DJANGO Channels: setup:

        ```
        1.pip install daphne
        2.ASGI_APPLICATION = 'Jahangir.asgi.application'
        ```
        3.asgi.py file ===============================================
                       import os

                        from django.core.asgi import get_asgi_application
                        from channels.routing import ProtocolTypeRouter,URLRouter
                        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Jahangir.settings')
                        import app.routring as r
                        application = ProtocolTypeRouter({
                            "http":get_asgi_application(),
                            'websocket':URLRouter(
                                r.websocket_urlspattens
                            )

                        })
                        ===========================================================
        
        4.django app create app.py 
                    then create routing.py ->
                            =======================================================

                            from django.urls import path
                            from . import consumers

                            websocket_urlspattens = [
                                path("ws/sc/",consumers.MySyncConsumer.as_asgi()),
                            ]

        
                    then create consumers.py file ->
                            =========================================================
                            from channels.consumer import SyncConsumer,AsyncConsumer
                            from channels.generic.websocket import AsyncWebsocketConsumer
                            from time import sleep
                            import asyncio

                            class MySyncConsumer(SyncConsumer):
                                def websocket_connect(self, event):
                                    print("Connected...",event)
                                    self.send({
                                        "type": "websocket.accept",        
                                    })
                                    
                                def websocket_receive(self,event):
                                    print("received by ...",event)
                                    print(event['text'])
                                    self.send({
                                        "type":"websocket.send",
                                        "text":"Bhaia kemon achen ?"
                                    })
                                    


                                def websocket_disconnect(self, event):
                                    print("Disconnected...",event)


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

                    

                
Server Side ->
    -> When Sending Data to client 
        . Python to String 

When Receiving Data From client
    -> String to Python


Python Json Lib 
    import Json  
        Json.dumps() - this method is used to convert Python dictionary into json String
        json.loads() - This method is used to convert json string into Python dictionary


JSON 
    JSON.parse() -> This method is used to convert json string into javascript  object 
    JSON.stringify() -> this method is used to convert javascript object into json string


 ws.onopen = (event) => {
            console.log("websocket conection open ...");
            ws.send("HI, Message from client ...")

        }

 ws.onmessage = (event) => {
            console.log("Message Recevied from server ..", event);
            document.getElementById("test").innerHTML = event.data;
        }




DJANGO CHANNELS LAYER:

    CHANNELS LAYER allow you to talk between differant instances of an application it is for heigh-level application to application communication . 

    A CHANNELS LAYER is transport  mechanism that allow multiple consumer instance to communicate with each other and other part DJANGO


    They are useful part making a  distributed real-time application if you don't want to have to shuttle all of your message or events through a database 

Redis CHANNELS LAYER ( always production level)
In-memory  CHANNELS LAYER




CHANNELS LAYER
--------------

    Channels -> Channels are first are first in first out queqe with at-most onec delivary ssemantics .Each Channels has name . Message are sent to Channels by anyone who knows the Channels name and the givan to consumerlistening on that Channels


    Group -> Sending to individual Channels isn't particularly useful - in most cases you 'll want to send to multiple Channels/consumer at onecas a  broadcast and there we use Group.
    removed from  a Group by anyone who knows the Group name.Using the Group name you can also send group are a broadcast system that =>
                                ->allow you ato add removed Channels names from nemed groups and send to those named groups
                                ->Provides group expired for clean-up conection whose disconnect handler did't get to run
    Message -> Message must be a dict . Because these message are sometimes sent over a network , they need to be serialiable

REDIS CHANNELS LAYER

        Redis works as the communication store for channels layer .
        In order to use Redis as a channels layer you have to install channels_redis package .
        channels_redis is the only offcial Djanog-maintained  Channels layer Supported for production use .
        The layer use Redis as tis backing store , and Support both a single-server and sharded configurations , as well as group Support . 
