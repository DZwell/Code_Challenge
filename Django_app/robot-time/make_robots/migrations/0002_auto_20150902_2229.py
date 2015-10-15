# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('make_robots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='agility',
            field=models.PositiveSmallIntegerField(default=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='robot',
            name='armour',
            field=models.PositiveSmallIntegerField(default=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='robot',
            name='strength',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
