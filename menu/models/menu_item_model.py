from django.db import models

from image.models import Image
from shared.models.soft_deletable_model import SoftDeletableModel


class MenuItem(SoftDeletableModel):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    item_images = models.ManyToManyField(to=Image, blank=True)

    def __str__(self):
        return self.name
