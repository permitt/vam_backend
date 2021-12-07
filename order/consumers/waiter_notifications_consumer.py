import json
from typing import Dict

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class WaiterNotificationsConsumer(JsonWebsocketConsumer):

    def connect(self, *args, **kwargs):
        waiter_id: int = self.scope['url_route']['kwargs']['waiter_id']
        self.user_room_name = 'waiter_' + waiter_id
        self.channel_layer.group_add(self.user_room_name, self.channel_name)
        self.accept()

    def receive_json(self, content, **kwargs):

        self.send_json(content)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.user_room_name,
            self.channel_name
        )

    def order_update(self, event):
        self.send_json(event)
        print(f'Primljena poruka {event} na kanalu {self.channel_name}')



