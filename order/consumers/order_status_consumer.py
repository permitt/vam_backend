import json
from typing import Dict

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class OrderStatusConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):

        order_id: int = self.scope['url_route']['kwargs']['order_id']
        self.order_group = 'order_' + order_id
        await self.accept()
        await self.channel_layer.group_add(self.order_group, self.channel_name)

    def receive_json(self, content, **kwargs):
        data: Dict = json.loads(content)
        print(data)
        self.send_json(data)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.order_group,
            self.channel_name
        )

    async def forward_group_message(self, event):
        await self.send(json.dumps(event['data'], default=str))


