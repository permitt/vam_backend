from rest_framework.serializers import  ModelSerializer

from image.serializers import ImageSerializer
from menu.models.menu_item_model import MenuItem


class MenuItemSerializer(ModelSerializer):
    item_images = ImageSerializer(many=True)

    class Meta:
        model = MenuItem
        fields = '__all__'
