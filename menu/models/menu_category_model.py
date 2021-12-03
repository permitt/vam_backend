from django.db import models
from menu.models.menu_item_model import MenuItem
from shared.models.soft_deletable_model import SoftDeletableModel


class MenuCategory(SoftDeletableModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    menu_items = models.ManyToManyField(to=MenuItem, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
