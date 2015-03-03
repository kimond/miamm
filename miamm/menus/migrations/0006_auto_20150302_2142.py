# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0005_auto_20150221_1107'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='menuuser',
            unique_together=set([('menu', 'user')]),
        ),
    ]
