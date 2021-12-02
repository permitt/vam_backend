from django.db import models

from client_facility.models import ClientFacility
from menu.models.menu_category_model import MenuCategory
from shared.models.soft_deletable_model import SoftDeletableModel


class Menu(SoftDeletableModel):
    description = models.TextField()
    menu_categories = models.ManyToManyField(to=MenuCategory)
    facility = models.ForeignKey(to=ClientFacility, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.facility.name}\'s menu - {self.description}'
