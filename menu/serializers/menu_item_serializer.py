from rest_framework.serializers import  ModelSerializer
from menu.models.menu_item_model import MenuItem


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
