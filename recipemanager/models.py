from django.db import models


# Create your models here.
class recipetype(models.Model):
    typename = models.CharField(null=False, max_length=45)

    def __unicode__(self):
        return self.typename


class unitlist(models.Model):
    unitname = models.CharField(null=False, max_length=45)


class ingredient(models.Model):
    name = models.CharField(null=False, max_length=75)
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.name


class step(models.Model):
    step_no = models.IntegerField(null=False)
    ingredient = models.ForeignKey('ingredient')
    quantity = models.IntegerField(null=False)
    unit = models.ForeignKey('unitlist')
    description = models.TextField(null=True)


class recipe(models.Model):
    name = models.CharField(null=False, max_length=100)
    description = models.TextField(null=True)
    steps = models.ManyToManyField('step')

    def __unicode__(self):
        return self.name



