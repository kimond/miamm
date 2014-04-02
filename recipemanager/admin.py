from django.contrib import admin
from recipemanager.models import Recipe, Step, RecipeIngredient
from recipemanager.forms import *

# Inlines

class RecipeIngredientInline(admin.TabularInline):
    form  = RecipeIngredientForm
    model = RecipeIngredient
    extra = 2


class StepInline(admin.TabularInline):
    form = StepForm
    model = Step
    extra = 2


class RecipeAdmin(admin.ModelAdmin):
    form = RecipeForm
    inlines = (RecipeIngredientInline, StepInline, )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(QuantityType)
