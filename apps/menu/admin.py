from django.contrib import admin

from .models import MenuItem, Menu


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 0


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline,]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass