from django.db import models
from shared.models.soft_deletable_manager import SoftDeletableManager


class SoftDeletableModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    non_deleted_objects = SoftDeletableManager()
    objects = models.Manager()
