from rest_framework.serializers import  ModelSerializer
from menu.models.menu_model import Menu


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
