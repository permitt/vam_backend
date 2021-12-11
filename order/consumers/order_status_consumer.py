import json
from typing import Dict

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class OrderStatusConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):

        order_id: str = self.scope['url_route']['kwargs']['order_id']
        self.order_group = 'order_' + order_id
        await self.accept()
        await self.channel_layer.group_add(self.order_group, self.channel_name)

    def receive_json(self, content, **kwargs):
        data: Dict = json.loads(content)
        print(data)
        self.send_json(data)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.order_group,
            self.channel_name
        )
        await self.close()

    async def forward_group_message(self, event):
        await self.send(json.dumps(event['data'], default=str))

    async def send_to_group(self, message):
        return self.channel_layer.group_send(self.order_group,
                                                            {"type": "forward.group.message",
                                                             "data": message})


