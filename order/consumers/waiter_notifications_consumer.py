import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class WaiterNotificationsConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self, *args, **kwargs):
        waiter_id: str = self.scope['url_route']['kwargs']['waiter_id']
        self.waiter_group = 'waiter_' + waiter_id
        await self.accept()
        await self.channel_layer.group_add(self.waiter_group, self.channel_name)

    def receive_json(self, content, **kwargs):
        self.send_to_group(content)
        self.send_json(content)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.waiter_group,
            self.channel_name
        )
        await self.close()

    async def forward_group_message(self, event):
        print(event, ' stigao')
        await self.send(json.dumps(event['data'], default=str))

    async def send_to_group(self, message):
        return self.channel_layer.group_send(self.waiter_group,
                                                            {"type": "forward.group.message",
                                                             "data": message})

    def order_update(self, event):
        self.send_json(event)
        print(f'Primljena poruka {event} na kanalu {self.channel_name}')



