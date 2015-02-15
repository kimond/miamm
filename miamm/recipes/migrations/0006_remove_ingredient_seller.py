# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20150215_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='seller',
        ),
    ]
