from django.contrib import admin

from order.models.order_item_model import OrderItem
from order.models.order_model import Order
from shared.models.admin_id_model import IdFieldAdmin

admin.site.register(Order, IdFieldAdmin)
admin.site.register(OrderItem, IdFieldAdmin)
