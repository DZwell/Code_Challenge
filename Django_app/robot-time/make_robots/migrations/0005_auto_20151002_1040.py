# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('make_robots', '0004_remove_robot_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='name',
            field=models.CharField(max_length=200, blank=True, null=True),
        ),
    ]
