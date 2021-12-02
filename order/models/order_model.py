from django.db import models

from order.models.order_item_model import OrderItem
from shared.models.soft_deletable_model import SoftDeletableModel
from table.models import Table
from waiter.models import Waiter


class Order(SoftDeletableModel):
    #status =
    table_order = models.ForeignKey(to=Table, on_delete=models.DO_NOTHING)
    waiter_assigned = models.ForeignKey(to=Waiter, on_delete=models.DO_NOTHING)
    order_items = models.ManyToManyField(to=OrderItem)
    date = models.DateTimeField(auto_created=True)
