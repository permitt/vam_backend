from typing import Dict

from rest_framework.serializers import ModelSerializer
from order.models.order_model import Order
from order.serializers.order_item_serializer import OrderItemSerializer


class OrderSerializer(ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order_items_created: Dict = self.create_order_items(validated_data.pop("order_items"))

        order: Order = Order.objects.create(**validated_data)

        [order.order_items.add(item['id']) for item in order_items_created]
        return order

    def create_order_items(self, order_items_data: Dict) -> Dict:
        order_item_objects = OrderItemSerializer(many=True, data=order_items_data)
        order_item_objects.is_valid()
        order_item_objects.save()
        return order_item_objects.data
