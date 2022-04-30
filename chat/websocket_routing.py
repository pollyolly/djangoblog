from django.urls import re_path, path
from . import websocket_consumers as consumers

websocket_urlpatterns = [
    #re_path(r'ws/djangoblog-socket/',consumers.ChatConsumer.as_asgi())    
    path('ws/djangoblog-socket/',consumers.ChatConsumer.as_asgi())    

]
