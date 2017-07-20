# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muo', '0032_historicaladvice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicaladvice',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicaladvice',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicaladvice',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='historicaladvice',
            name='muo',
        ),
        migrations.DeleteModel(
            name='HistoricalAdvice',
        ),
    ]
