from rest_framework.serializers import ModelSerializer
from client_facility.models import ClientFacility


class ClientFacilitySerializer(ModelSerializer):
    class Meta:
        model = ClientFacility
        fields = '__all__'
