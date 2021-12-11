from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response

from shared.models.custom_api_view import CustomAPIView


class ImageView(CustomAPIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        pass
