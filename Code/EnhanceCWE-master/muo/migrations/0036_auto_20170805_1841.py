# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muo', '0035_auto_20170805_1814'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advice',
            options={'default_permissions': ('view',), 'verbose_name': 'Advice', 'verbose_name_plural': 'Advices'},
        ),
    ]
