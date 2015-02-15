# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20150208_1525'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='week',
            unique_together=set([('menu', 'number')]),
        ),
    ]
