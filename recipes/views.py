from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework import generics
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
