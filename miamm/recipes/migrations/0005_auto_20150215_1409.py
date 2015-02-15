# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20150129_0737'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='step',
            unique_together=set([('recipe', 'order')]),
        ),
    ]
