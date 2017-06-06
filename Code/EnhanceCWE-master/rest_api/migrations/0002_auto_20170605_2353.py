# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restconfiguration',
            name='active',
            field=models.BooleanField(default=True, db_index=True),
        ),
        migrations.AddField(
            model_name='restconfiguration',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='restconfiguration',
            name='created_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='restconfiguration',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 23, 53, 12, 315783, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restconfiguration',
            name='modified_by',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
