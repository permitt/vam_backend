from django.contrib.auth.models import User
from django.db import models
from shared.models.soft_deletable_model import SoftDeletableModel


class Waiter(SoftDeletableModel):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} {self.last_name}'
