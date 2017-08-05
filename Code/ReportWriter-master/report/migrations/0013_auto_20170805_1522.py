# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0012_advice'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advice',
            options={'default_permissions': (), 'verbose_name': 'Advice', 'verbose_name_plural': 'Advice'},
        ),
    ]
