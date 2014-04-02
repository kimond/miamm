from django.views.generic import TemplateView
from django.shortcuts import render
from recipemanager.models import Recipe

def main(request):

    recipes = Recipe.objects.all()
    context = {
        "recipes" : recipes
    }
    return render(request,"recipemanager/recipemain.html", context)


def viewrecipe(request, *args, **kwargs):
    recipeId = kwargs.get("recipeId")

    try:
        recipe = Recipe.objects.get(id=recipeId)
    except Recipe.DoesNotExist:
        return ""

    context = {
        "recipe": recipe
    }
    return render(request, "recipemanager/recipeview.html", context)
