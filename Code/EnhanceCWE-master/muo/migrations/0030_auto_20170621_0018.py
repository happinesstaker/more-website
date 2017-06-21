# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muo', '0029_auto_20170614_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='muo',
            field=models.ForeignKey(related_name='muocontainer_id', on_delete=django.db.models.deletion.PROTECT, to='muo.MUOContainer'),
        ),
    ]
