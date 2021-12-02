from django.contrib import admin

from order.models.order_item_model import OrderItem
from order.models.order_model import Order

admin.site.register(Order)
admin.site.register(OrderItem)
