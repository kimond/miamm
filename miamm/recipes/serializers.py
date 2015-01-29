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
    ingredient = IngredientSerializer(many=False, read_only=False)
    quantity_type = QuantityTypeSerializer(many=False, read_only=False)

    class Meta:
        model = RecipeIngredient
        fields = ('ingredient', 'quantity', 'quantity_type')

    def create(self, validated_data):
        ingredient_data = validated_data.pop('ingredient')
        quantity_type_data = validated_data.pop('quantity_type')
        ingredient = Ingredient.objects.get(name=ingredient_data['name'])
        quantity_type = QuantityType.objects.get(name=quantity_type_data['name'])
        recipeingredient = RecipeIngredient.objects.create(ingredient=ingredient,quantity_type=quantity_type, **validated_data)

        return recipeingredient


class StepListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        steps = [Step(**item) for item in validated_data]
        return Step.objects.bulk_create(steps)

    def update(self, instance, validated_data):
        # Maps for id->instance and id->data item.
        step_mapping = {step.id: step for step in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for step_id, data in data_mapping.items():
            step = step_mapping.get(step_id, None)
            if step is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(step, data))

        # Perform deletions.
        for step_id, step in step_mapping.items():
            if step_id not in data_mapping:
                step.delete()

        return ret


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ('order', 'explanation')
        #list_serializer_class = StepListSerializer


class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True, read_only=True)
    ingredients = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'prepare_time', 'cook_time', 'portion', 'comment', 'steps', 'ingredients')
        depth = 1

    # def create(self, validated_data):
    #     steps_data = validated_data.pop('steps')
    #     recipe = Recipe.objects.create(**validated_data)
    #     Step.objects.create(recipe=recipe, **steps_data)
    #     return recipe

    # def update(self, instance, validated_data):
    #     steps_data = validated_data.pop('steps')
    #     # Unless the application properly enforces that this field is
    #     # always set, the follow could raise a `DoesNotExist`, which
    #     # would need to be handled.
    #     steps = instance.steps
    #
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.prepare_time = validated_data.get('prepare_time', instance.prepare_time)
    #     instance.save()
    #
    #     for step in steps.all():
    #         step.save()
    #
    #     return instance
