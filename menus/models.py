from django.db import models
from recipes.models import Recipe
# Create your models here.

class Day(models.Model):
    dinner = models.ForeignKey(Recipe, related_name='dinner')
    supper = models.ForeignKey(Recipe, related_name='supper')

    def __unicode__(self):
        return self.dinner.name + ", " + self.supper.name


class Week(models.Model):
    number = models.IntegerField(null=True)
    days = models.ManyToManyField(Day)
