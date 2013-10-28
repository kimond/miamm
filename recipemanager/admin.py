from django.contrib import admin
from models import ingredient, recipe, unitlist, recipetype, step


admin.site.register(ingredient)
admin.site.register(unitlist)
admin.site.register(recipetype)
admin.site.register(recipe)
admin.site.register(step)
