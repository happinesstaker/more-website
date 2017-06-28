# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('muo', '0030_auto_20170621_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('created_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True)),
                ('modified_by', models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True)),
                ('usecase', models.ForeignKey(related_name='vote_usecase_id', on_delete=django.db.models.deletion.PROTECT, to='muo.UseCase')),
                ('user', models.ForeignKey(related_name='vote_user_id', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
