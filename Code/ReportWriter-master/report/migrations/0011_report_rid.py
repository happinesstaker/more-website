# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0010_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='rid',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
