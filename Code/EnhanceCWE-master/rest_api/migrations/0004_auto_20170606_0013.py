# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_restconfiguration_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restconfiguration',
            name='name',
            field=models.CharField(unique=True, max_length=32),
        ),
    ]
