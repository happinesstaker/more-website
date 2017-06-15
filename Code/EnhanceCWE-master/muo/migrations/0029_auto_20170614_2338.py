# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muo', '0028_auto_20170614_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='muocontainer',
            old_name='rw_identifier',
            new_name='rid',
        ),
    ]
