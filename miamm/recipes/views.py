from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework import generics
from recipes.models import Recipe, Step, RecipeIngredient
from recipes.serializers import RecipeSerializer, StepSerializer, RecipeIngredientSerializer
from django.shortcuts import get_object_or_404


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
        This view should return a list of all steps for a recipe
        """
        recipe_id = self.kwargs['pk']
        return Step.objects.filter(recipe=recipe_id)

    def perform_create(self, serializer):
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        serializer.save(recipe=recipe)


class StepDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Step
    serializer_class = StepSerializer

    def get_queryset(self):
        """
        This view should return a step in a recipe
        """
        recipe_id = self.kwargs['pk']
        step_order = self.kwargs['step_order']
        return Step.objects.filter(order=step_order, recipe=recipe_id)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj



class RecipeIngredientList(generics.ListCreateAPIView):
    model = RecipeIngredient
    serializer_class = RecipeIngredientSerializer

    def get_queryset(self):
        """
        This view should return a list of all ingredients for a recipe
        """
        recipe_id = self.kwargs['pk']
        return RecipeIngredient.objects.filter(recipe=recipe_id)

    def perform_create(self, serializer):
        recipe = Recipe.objects.get(pk=self.kwargs['pk'])
        serializer.save(recipe=recipe)


class RecipeIngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    model = RecipeIngredient
    serializer_class = RecipeIngredientSerializer

    def get_queryset(self):
        """
        This view should return an ingredient for a recipe
        """
        recipe_id = self.kwargs['pk']
        recipeingredient_id = self.kwargs['recipeingredient_pk']
        return RecipeIngredient.objects.filter(pk=recipeingredient_id)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset)
        return obj
