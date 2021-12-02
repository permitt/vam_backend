from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import QuerySet


class SoftDeletableManager(models.Manager):
    def all(self) -> QuerySet:
        return super().get_queryset().filter(is_deleted=False)

    def get(self, obj_id: int):
        obj = super().get_queryset().get(id=obj_id)

        if obj.is_deleted:
            raise ObjectDoesNotExist

        return obj
