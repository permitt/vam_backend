from typing import List

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.response import Response
from order.models.order_model import Order
from order.serializers.order_serializer import OrderSerializer
from shared.models.custom_api_view import CustomAPIView


class OrderView(CustomAPIView):
    model = Order
    serializer = OrderSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        if 'id' in kwargs:
            return self.get_by_id(kwargs['id'])
        else:
            return self.get_all(request)

    def get_by_id(self, id: int) -> Response:
        data: Order = self.model.non_deleted_objects.get(id)
        return Response(self.serializer(data).data, status=status.HTTP_200_OK)

    def get_all(self, request: Request) -> Response:
        data: QuerySet[Order] = self.get_queryset().order_by('name')

        data: List[Order] = self.paginator.paginate_queryset(data, request)
        return self.paginator.get_paginated_response(self.serializer(data, many=True).data)
