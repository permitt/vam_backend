from rest_framework.serializers import  ModelSerializer
from menu.models.menu_model import Menu
from menu.serializers.menu_category_serializer import MenuCategorySerializer


class MenuSerializer(ModelSerializer):
    menu_categories = MenuCategorySerializer(many=True)

    class Meta:
        model = Menu
        fields = '__all__'
