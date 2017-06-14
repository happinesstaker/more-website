# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muo', '0027_advice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advice',
            old_name='advice',
            new_name='advice_text',
        ),
        migrations.AddField(
            model_name='advice',
            name='advice_title',
            field=models.CharField(default='Untitled', max_length=50),
            preserve_default=False,
        ),
    ]
