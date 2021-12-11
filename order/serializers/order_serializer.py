from typing import Dict

from rest_framework.serializers import ModelSerializer
from order.models.order_model import Order
from order.serializers.order_item_serializer import OrderItemSerializer


class OrderSerializer(ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'table_order', 'waiter_assigned', 'order_items', 'date', 'status')

    def create(self, validated_data):
        print(validated_data)
        order_items_data = validated_data.pop('order_items')
        order: Order = Order.objects.create(**validated_data)
        order_item_serializer = self.fields['order_items']
        for item in order_items_data:
            item['order_id'] = order
        order_items = order_item_serializer.create(order_items_data)
        validated_data['order_items'] = order_items
        return order

    def create_order_items(self, order_items_data: Dict) -> Dict:
        order_item_objects = OrderItemSerializer(many=True, data=order_items_data)
        order_item_objects.is_valid()
        order_item_objects.save()
        return order_item_objects.data
