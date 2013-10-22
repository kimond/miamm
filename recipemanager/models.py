from django.db import models


# Create your models here.
class recipetype(models.Model):
    typename = models.CharField(null=False)

    def __unicode__(self):
        return self.typename


class step(models.Model):
    step_no = models.IntegerField(null=False)


class recipe(models.Model):
    name = models.CharField(null=False)
    description = models.TextField(null=True)

    def __unicode__(self):
        return self.name



