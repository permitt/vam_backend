from django.db import models

from menu.models.menu_item_model import MenuItem
from shared.models.soft_deletable_model import SoftDeletableModel


class OrderItem(SoftDeletableModel):
    amount = models.IntegerField(default=1)
    menu_item = models.ForeignKey(to=MenuItem, on_delete=models.DO_NOTHING)
