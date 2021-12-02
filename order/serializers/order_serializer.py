from rest_framework.serializers import ModelSerializer
from order.models.order_model import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
