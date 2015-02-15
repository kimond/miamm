# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='week',
            name='days',
        ),
        migrations.AddField(
            model_name='week',
            name='friday',
            field=models.ForeignKey(related_name='friday', default=None, to='menus.Day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='menu',
            field=models.ForeignKey(related_name='weeks', default=None, to='menus.Menu'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='monday',
            field=models.ForeignKey(related_name='monday', default=None, to='menus.Day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='saturday',
            field=models.ForeignKey(related_name='saturday', default=None, to='menus.Day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='sunday',
            field=models.ForeignKey(related_name='sunday', default=None, to='menus.Day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='thursday',
            field=models.ForeignKey(related_name='thursday', default=None, to='menus.Day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='tuesday',
            field=models.ForeignKey(related_name='tuesday', default=None, to='menus.Day'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='week',
            name='wednesday',
            field=models.ForeignKey(related_name='wednesday', default=None, to='menus.Day'),
            preserve_default=False,
        ),
    ]
