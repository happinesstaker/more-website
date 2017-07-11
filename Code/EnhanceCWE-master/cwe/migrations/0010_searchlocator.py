# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cwe', '0009_auto_20150618_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchLocator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Default', max_length=128)),
            ],
            options={
                'verbose_name': 'SearchLocator',
            },
        ),
    ]
