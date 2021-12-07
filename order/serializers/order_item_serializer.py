from rest_framework.serializers import ModelSerializer

from menu.serializers.menu_item_serializer import MenuItemSerializer
from order.models.order_item_model import OrderItem


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'amount', 'menu_item')

