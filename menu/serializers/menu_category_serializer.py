from rest_framework.serializers import  ModelSerializer
from menu.models.menu_category_model import MenuCategory
from menu.serializers.menu_item_serializer import MenuItemSerializer


class MenuCategorySerializer(ModelSerializer):
    menu_items = MenuItemSerializer(many=True)

    class Meta:
        model = MenuCategory
        fields = '__all__'
