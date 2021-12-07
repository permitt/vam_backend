from django.db import models

from menu.models.menu_item_model import MenuItem
from order.models.order_model import Order
from shared.models.soft_deletable_model import SoftDeletableModel


class OrderItem(SoftDeletableModel):
    amount = models.IntegerField(default=1)
    menu_item = models.ForeignKey(to=MenuItem, on_delete=models.DO_NOTHING)
    order_id = models.ForeignKey(to=Order, related_name='order_items', on_delete=models.DO_NOTHING, blank=True)
