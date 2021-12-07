from django.contrib import admin

from shared.models.admin_id_model import IdFieldAdmin
from waiter.models import Waiter

admin.site.register(Waiter, IdFieldAdmin)

