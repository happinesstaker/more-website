# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muo', '0036_auto_20170805_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advice',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'verbose_name': 'Advice', 'verbose_name_plural': 'Advices'},
        ),
    ]
