# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0013_auto_20170805_1522'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advice',
            options={'verbose_name': 'Advice', 'verbose_name_plural': 'Advices'},
        ),
    ]
