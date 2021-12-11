import json
from typing import List, Dict

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from channels_redis.core import RedisChannelLayer
from django.db.models import QuerySet
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from order.models.order_model import Order
from order.serializers.order_serializer import OrderSerializer
from shared.enums.order_status_enum import OrderStatus
from shared.models.custom_api_view import CustomAPIView


class OrderView(CustomAPIView):
    model = Order
    serializer = OrderSerializer
    channel_layer: RedisChannelLayer = get_channel_layer()

    def get(self, request: Request, *args, **kwargs) -> Response:
        if 'id' in kwargs:
            return self.get_by_id(kwargs['id'])
        else:
            return self.get_all(request)

    def get_by_id(self, id: int) -> Response:
        data: Order = self.model.non_deleted_objects.get(id)
        return Response(self.serializer(data).data, status=status.HTTP_200_OK)

    def get_all(self, request: Request) -> Response:
        data: QuerySet[Order] = self.get_queryset().order_by('-date')

        data: List[Order] = self.paginator.paginate_queryset(data, request)
        return self.paginator.get_paginated_response(self.serializer(data, many=True).data)

    def put(self, request: Request, *args, **kwargs) -> Response:
        obj_id: int = kwargs.get('id', -1)
        instance: Order = self.model.non_deleted_objects.get(obj_id)

        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        instance.status = OrderStatus(instance.status.value + 1)
        instance.save()

        message: Dict = {"table_name": instance.table_order.name, "id": instance.id.__str__(),
                         "table": instance.table_order.table_id.__str__(),
                         "date": json.dumps(instance.date, cls=DjangoJSONEncoder),
                         "status": instance.status}

        channel_name: str = f'order_{instance.id}'
        async_to_sync(self.channel_layer.group_send)(channel_name,
                                                     {"type": "forward.group.message",
                                                      "data": message})

        return Response(status=status.HTTP_200_OK)

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        order: Order = serializer.create(serializer.validated_data)

        message: Dict = {"table_name": order.table_order.name, "id": order.id.__str__(),
                         "table": order.table_order.table_id.__str__(),
                         "date": json.dumps(order.date, cls=DjangoJSONEncoder),
                         "status": OrderStatus.RECEIVED}

        channel_name: str = f'waiter_{order.waiter_assigned_id}'
        async_to_sync(self.channel_layer.group_send)(channel_name,
                                                     {"type": "forward.group.message",
                                                      "data": message})
        return Response(self.serializer(order).data, status=status.HTTP_201_CREATED)
