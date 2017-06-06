# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_auto_20170605_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='restconfiguration',
            name='name',
            field=models.CharField(default=datetime.datetime(2017, 6, 5, 23, 58, 44, 490055, tzinfo=utc), max_length=32),
            preserve_default=False,
        ),
    ]
