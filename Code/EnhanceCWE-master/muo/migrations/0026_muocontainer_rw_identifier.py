# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muo', '0025_muocontainer_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='muocontainer',
            name='rw_identifier',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
