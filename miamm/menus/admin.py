from django.contrib import admin
from menus.models import Day, Week, Menu, MenuUser


class MenuUserInline(admin.TabularInline):
    model = MenuUser
    extra = 2

class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuUserInline, )

admin.site.register(Menu, MenuAdmin)
admin.site.register(Day)
admin.site.register(Week)
