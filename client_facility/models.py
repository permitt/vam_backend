from django.db import models
from shared.models.soft_deletable_model import SoftDeletableModel


class ClientFacility(SoftDeletableModel):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "client facilities"

    def __str__(self):
        return self.name
