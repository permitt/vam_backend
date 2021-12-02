from rest_framework.serializers import  ModelSerializer
from menu.models.menu_category_model import MenuCategory


class MenuCategorySerializer(ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = '__all__'
