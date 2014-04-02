from django import forms
from recipemanager.models import *


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient


class StepForm(forms.ModelForm):
    class Meta:
        model = Step


class RecipeForm(forms.ModelForm):
     class Meta:
         model = Recipe
