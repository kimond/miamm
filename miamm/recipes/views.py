from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework import generics
from recipes.models import Recipe, Step, RecipeIngredient
from recipes.serializers import RecipeSerializer, StepSerializer, RecipeIngredientSerializer


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class StepList(generics.ListCreateAPIView):
    model = Step
    serializer_class = StepSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        recipe_id = self.kwargs['pk']
        return Step.objects.filter(recipe=recipe_id)

    def perform_create(self, serializer):
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        serializer.save(recipe=recipe)


class RecipeIngredientList(generics.ListCreateAPIView):
    model = RecipeIngredient
    serializer_class = RecipeIngredientSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        recipe_id = self.kwargs['pk']
        return RecipeIngredient.objects.filter(recipe=recipe_id)

    def perform_create(self, serializer):
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        serializer.save(recipe=recipe)
