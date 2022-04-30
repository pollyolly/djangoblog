import json
from datetime import date
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        """
        today = date.today()
        datenow = today.strftime("%B %d, %Y")

        self.send(text_data=json.dumps({
            'type':'chat',
            'name':'Server',
            'date':datenow,
            'message':'Connectio was established!'
        }))
        """
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        name = text_data_json['name']

        #print('Message:', message)

        today = date.today()
        datenow = today.strftime("%B %d, %Y")

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                'type':'chat_message',
                'name':name,
                'date':datenow,
                'message': message
            }
        )
    def chat_message(self, event):
        name = event['name']
        datenow = event['date']
        message = event['message']
         
        self.send(text_data=json.dumps({
            'type':'chat',
            'name':name,
            'date':datenow,
            'message': message
        })) 

#    def disconnect(self,close_code):
#        pass        
