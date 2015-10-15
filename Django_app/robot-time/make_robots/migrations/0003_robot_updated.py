# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('make_robots', '0002_auto_20150902_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 16, 38, 34, 828215, tzinfo=utc), verbose_name=datetime.datetime(2015, 9, 22, 16, 37, 49, 277415, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
