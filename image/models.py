from django.db import models
from shared.models.soft_deletable_model import SoftDeletableModel


class Image(SoftDeletableModel):
    caption = models.TextField()
    file = models.ImageField(upload_to='images', default='default.jpg')

    def __str__(self):
        return self.caption
