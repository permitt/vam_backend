from django.db import models
from shared.enums.order_status_enum import OrderStatus
from shared.models.soft_deletable_model import SoftDeletableModel
from table.models import Table
from waiter.models import Waiter


class Order(SoftDeletableModel):
    table_order = models.ForeignKey(to=Table, on_delete=models.DO_NOTHING)
    waiter_assigned = models.ForeignKey(to=Waiter, on_delete=models.DO_NOTHING, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=15,
        choices=OrderStatus.choices,
        default=OrderStatus.RECEIVED,
    )

