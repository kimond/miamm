# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20150128_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='seller',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
