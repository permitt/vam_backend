import json
from typing import Dict

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class OrderStatusConsumer(JsonWebsocketConsumer):

    def connect(self):

        order_id: int = self.scope['url_route']['kwargs']['order_id']
        self.user_room_name = 'order_' + order_id
        self.channel_layer.group_add(self.user_room_name, self.channel_name)
        self.accept()

    def receive_json(self, content, **kwargs):
        data: Dict = json.loads(content)
        print(data)
        self.send_json(data)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.user_room_name,
            self.channel_name
        )

    def order_update(self, event):
        self.send_json(event)
        print(f'Primljena poruka {event} na kanalu {self.channel_name}')



