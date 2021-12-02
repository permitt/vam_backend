from abc import ABC, abstractmethod
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.serializers import ModelSerializer
from shared.models.soft_deletable_model import SoftDeletableModel


class CustomAPIView(APIView, ABC):
    model = SoftDeletableModel
    serializer = ModelSerializer

    def __init__(self):
        self.paginator = PageNumberPagination()
        self.paginator.page_size = 10
        self.paginator.page_size_query_param = 'page_size'

    def get_queryset(self):
        return self.model.non_deleted_objects.all()

    @abstractmethod
    def get(self, request: Request, *args, **kwargs) -> Response:
        pass

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request: Request, *args, **kwargs) -> Response:
        obj_id: int = kwargs.get('id', -1)
        instance = self.model.non_deleted_objects.get(obj_id)

        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer(instance, data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, *args, **kwargs) -> Response:
        obj_id: int = kwargs.get('id', -1)
        instance = self.model.non_deleted_objects.get(obj_id)

        if instance is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
