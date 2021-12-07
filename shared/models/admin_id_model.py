from django.contrib import admin

class IdFieldAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

