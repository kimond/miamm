from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


class Day(models.Model):
    dinner = models.ForeignKey(Recipe, related_name='dinner')
    supper = models.ForeignKey(Recipe, related_name='supper')

    def __unicode__(self):
        return self.dinner.name + ", " + self.supper.name


class Menu(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name='owner')

    def __unicode__(self):
        return self.name


class Week(models.Model):
    menu = models.ForeignKey(Menu, related_name='weeks')
    number = models.IntegerField(null=True)
    sunday = models.ForeignKey(Day, related_name='sunday')
    monday = models.ForeignKey(Day, related_name='monday')
    tuesday = models.ForeignKey(Day, related_name='tuesday')
    wednesday = models.ForeignKey(Day, related_name='wednesday')
    thursday = models.ForeignKey(Day, related_name='thursday')
    friday = models.ForeignKey(Day, related_name='friday')
    saturday = models.ForeignKey(Day, related_name='saturday')

    def __unicode__(self):
        return self.menu.name + ' - ' + str(self.number)

    class Meta:
        unique_together = ("menu", "number")


class MenuUser(models.Model):
    menu = models.ForeignKey(Menu, related_name='users')
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ("menu", "user")
