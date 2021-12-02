from django.db import models
from shared.models.soft_deletable_model import SoftDeletableModel


class Image(SoftDeletableModel):
    path = models.CharField(max_length=150)
    caption = models.TextField()
    file = models.ImageField(upload_to='data_images/')
