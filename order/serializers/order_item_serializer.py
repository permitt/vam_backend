from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from menu.serializers.menu_item_serializer import MenuItemSerializer
from order.models.order_item_model import OrderItem


class OrderItemSerializer(ModelSerializer):
    name = serializers.ReadOnlyField(source='menu_item.name')
    price = serializers.ReadOnlyField(source='menu_item.price')

    class Meta:
        model = OrderItem
        fields = ('id', 'amount', 'menu_item', 'name', 'price')
