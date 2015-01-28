from rest_framework import serializers
from recipes.models import Recipe, Step, RecipeIngredient, Ingredient, QuantityType


class QuantityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityType
        fields = ('name',)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)
    quantity_type = QuantityTypeSerializer(many=False, read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'quantity', 'quantity_type')


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('order', 'explanation')


class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    ingredients = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'prepare_time', 'cook_time', 'portion', 'comment', 'steps', 'ingredients')
