from typing import List

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from client_facility.models import ClientFacility
from client_facility.serializers import ClientFacilitySerializer
from shared.models.custom_api_view import CustomAPIView


class ClientFacilityView(CustomAPIView):
    model = ClientFacility
    serializer = ClientFacilitySerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        if 'id' in kwargs:
            return self.get_by_id(kwargs['id'])
        else:
            return self.get_all(request)

    def get_by_id(self, id: int) -> Response:
        data: ClientFacility = self.model.non_deleted_objects.get(id)
        return Response(self.serializer(data).data, status=status.HTTP_200_OK)

    def get_all(self, request: Request) -> Response:
        data: QuerySet[ClientFacility] = self.get_queryset().order_by('name')

        data: List[ClientFacility] = self.paginator.paginate_queryset(data, request)
        return self.paginator.get_paginated_response(self.serializer(data, many=True).data)
