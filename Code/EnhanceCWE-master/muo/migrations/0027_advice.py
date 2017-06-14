# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('muo', '0026_muocontainer_rw_identifier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('advice', models.CharField(max_length=1000)),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True)),
                ('muo', models.ForeignKey(related_name='muocontainer_id', to='muo.MUOContainer')),
            ],
            options={
                'default_permissions': 'view',
                'verbose_name': 'Advice',
                'verbose_name_plural': 'Advice',
            },
        ),
    ]
