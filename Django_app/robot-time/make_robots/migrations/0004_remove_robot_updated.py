# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('make_robots', '0003_robot_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robot',
            name='updated',
        ),
    ]
