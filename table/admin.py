from django.contrib import admin
from table.models import Table

class TableAdmin(admin.ModelAdmin):
    readonly_fields = ('table_id',)

admin.site.register(Table, TableAdmin)
