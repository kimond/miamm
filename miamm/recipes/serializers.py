from rest_framework import serializers, fields
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
    ingredient = IngredientSerializer(many=False, read_only=False)
    quantity_type = QuantityTypeSerializer(many=False, read_only=False)

    class Meta:
        model = RecipeIngredient
        fields = ('id','ingredient', 'quantity', 'quantity_type')

    def create(self, validated_data):
        ingredient_data = validated_data.pop('ingredient')
        quantity_type_data = validated_data.pop('quantity_type')
        ingredient = Ingredient.objects.get(name=ingredient_data['name'])
        quantity_type = QuantityType.objects.get(name=quantity_type_data['name'])
        recipeingredient = RecipeIngredient.objects.create(ingredient=ingredient,quantity_type=quantity_type, **validated_data)

        return recipeingredient

    def update(self, instance, validated_data):
        ingredient_data = validated_data.pop('ingredient')
        quantity_type_data = validated_data.pop('quantity_type')
        ingredient = Ingredient.objects.get(name=ingredient_data['name'])
        quantity_type = QuantityType.objects.get(name=quantity_type_data['name'])

        if instance.ingredient != ingredient:
            instance.ingredient = ingredient

        if instance.quantity_type != quantity_type:
            instance.quantity_type = quantity_type

        instance.quantity = validated_data.get('quantity')
        instance.save()

        return instance


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('order', 'explanation')

    def create(self, validated_data):
        recipe = validated_data.get('recipe')
        step_order = validated_data.get('order')
        existing_step = Step.objects.filter(recipe=recipe, order=step_order)
        if len(existing_step) > 0:
            raise serializers.ValidationError('This is already a step number '+str(step_order))

        return super(StepSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        step_order = validated_data.get('order')
        if step_order != instance.order:
            recipe = instance.recipe
            existing_step = Step.objects.filter(recipe=recipe, order=step_order)
            if len(existing_step) > 0:
                raise serializers.ValidationError('This is already a step number '+str(step_order))

        return super(StepSerializer, self).update(instance, validated_data)


class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    ingredients = RecipeIngredientSerializer(many=True, read_only=True)
    url = fields.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'prepare_time', 'cook_time', 'portion', 'comment', 'steps', 'ingredients','url')
        depth = 1
