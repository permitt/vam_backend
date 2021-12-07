from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatus(models.TextChoices):
    RECEIVED = 'RECEIVED', _('Received')
    IN_PROGRESS = 'IN_PROGRESS', _('In progress')
    PREPARED = 'PREPARED', _('Prepared')
    SERVED = 'SERVED', _('Served')
    PAID = 'PAID', _('Paid')

