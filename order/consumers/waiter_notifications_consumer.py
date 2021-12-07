import json
from typing import Dict

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from channels.layers import get_channel_layer


class WaiterNotificationsConsumer(JsonWebsocketConsumer):

    def connect(self, *args, **kwargs):
        waiter_id: str = self.scope['url_route']['kwargs']['waiter_id']
        self.waiter_group = 'waiter_' + waiter_id
        self.channel_layer.group_add(self.waiter_group, self.channel_name)
        self.accept()

    def receive_json(self, content, **kwargs):
        channel_layer = get_channel_layer()
        channel_layer.send(self.waiter_group, {"PICKO":"MRS"})
        async_to_sync(channel_layer.group_send)(self.waiter_group, content)
        self.send_json(content)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.waiter_group,
            self.channel_name
        )
        self.close()

    def order_update(self, event):
        self.send_json(event)
        print(f'Primljena poruka {event} na kanalu {self.channel_name}')



