# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cwe', '0011_historicalcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalcategory',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalcategory',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalcategory',
            name='modified_by',
        ),
        migrations.DeleteModel(
            name='HistoricalCategory',
        ),
    ]
