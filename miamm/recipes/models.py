from django.db import models


class QuantityType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True)
    prepare_time = models.IntegerField(null=True, blank=True)
    cook_time = models.IntegerField(null=True, blank=True)
    portion = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)

    def get_view_url(self):
        pass

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    seller = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.IntegerField()
    quantity_type = models.ForeignKey(QuantityType)



class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps')
    order = models.IntegerField()
    explanation = models.TextField()
