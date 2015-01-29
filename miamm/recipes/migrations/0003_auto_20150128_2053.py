# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20150125_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(related_name='ingredients', to='recipes.Recipe'),
            preserve_default=True,
        ),
    ]
