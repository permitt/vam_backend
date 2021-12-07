from django.contrib import admin
from menu.models.menu_category_model import MenuCategory
from menu.models.menu_item_model import MenuItem
from menu.models.menu_model import Menu
from shared.models.admin_id_model import IdFieldAdmin

admin.site.register(Menu, IdFieldAdmin)
admin.site.register(MenuCategory, IdFieldAdmin)
admin.site.register(MenuItem, IdFieldAdmin)
