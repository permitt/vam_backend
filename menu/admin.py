from django.contrib import admin
from menu.models.menu_category_model import MenuCategory
from menu.models.menu_item_model import MenuItem
from menu.models.menu_model import Menu

admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
