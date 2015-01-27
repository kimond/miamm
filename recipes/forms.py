from django import forms
from recipes.models import *


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = '__all__'


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = '__all__'


class RecipeForm(forms.ModelForm):
     class Meta:
         model = Recipe
         fields = '__all__'
