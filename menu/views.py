from typing import List
from django.db.models import QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from menu.models.menu_model import Menu
from menu.serializers.menu_serializer import MenuSerializer
from shared.models.custom_api_view import CustomAPIView


class MenuView(CustomAPIView):
    model = Menu
    serializer = MenuSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        if 'id' in kwargs:
            return self.get_by_facility_id(kwargs['id'])
        else:
            return self.get_all(request)

    def get_by_facility_id(self, facility_id: int) -> Response:
        data: Menu = self.model.non_deleted_objects.filter(facility__pk=facility_id).first()
        return Response(self.serializer(data).data, status=status.HTTP_200_OK) if data else Response(
            status=status.HTTP_400_BAD_REQUEST)

    def get_all(self, request: Request) -> Response:
        data: QuerySet[Menu] = self.get_queryset().order_by('id').filter(
            description__contains=request.query_params.get('description', '')
        )

        data: List[Menu] = self.paginator.paginate_queryset(data, request)
        return self.paginator.get_paginated_response(self.serializer(data, many=True).data)
