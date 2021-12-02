from rest_framework.serializers import ModelSerializer

from order.models.order_item_model import OrderItem


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
