import uuid

from django.db import models
from client_facility.models import ClientFacility
from shared.models.soft_deletable_model import SoftDeletableModel
from waiter.models import Waiter


class Table(SoftDeletableModel):
    table_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    number = models.IntegerField()
    assigned_to = models.ForeignKey(to=Waiter, on_delete=models.DO_NOTHING)
    facility = models.ForeignKey(to=ClientFacility, on_delete=models.DO_NOTHING)
