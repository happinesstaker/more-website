# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('muo', '0031_vote'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalMUOContainer',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified_at', models.DateTimeField(editable=False, blank=True)),
                ('active', models.BooleanField(default=True, db_index=True)),
                ('name', models.CharField(default=b'/', max_length=16, null=True, db_index=True, blank=True)),
                ('misuse_case_type', models.CharField(default=b'new', max_length=16, null=True, verbose_name=b'Misuse Case Type', choices=[(b'existing', b'Existing'), (b'new', b'New')])),
                ('misuse_case_name', models.CharField(default=b'/', max_length=16, null=True, db_index=True, blank=True)),
                ('misuse_case_description', models.TextField(null=True, verbose_name=b'Brief Description', blank=True)),
                ('misuse_case_primary_actor', models.CharField(max_length=256, null=True, verbose_name=b'Primary actor', blank=True)),
                ('misuse_case_secondary_actor', models.CharField(max_length=256, null=True, verbose_name=b'Secondary actor', blank=True)),
                ('misuse_case_precondition', models.TextField(null=True, verbose_name=b'Pre-condition', blank=True)),
                ('misuse_case_flow_of_events', models.TextField(null=True, verbose_name=b'Flow of events', blank=True)),
                ('misuse_case_postcondition', models.TextField(null=True, verbose_name=b'Post-condition', blank=True)),
                ('misuse_case_assumption', models.TextField(null=True, verbose_name=b'Assumption', blank=True)),
                ('misuse_case_source', models.TextField(null=True, verbose_name=b'Source', blank=True)),
                ('reject_reason', models.TextField(null=True, blank=True)),
                ('status', models.CharField(default=b'draft', max_length=64, choices=[(b'draft', b'Draft'), (b'in_review', b'In Review'), (b'approved', b'Approved'), (b'rejected', b'Rejected')])),
                ('is_custom', models.BooleanField(default=False, db_index=True)),
                ('is_published', models.BooleanField(default=False, db_index=True)),
                ('rid', models.CharField(max_length=256, null=True, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('created_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
                ('misuse_case', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='muo.MisuseCase', null=True)),
                ('modified_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('reviewed_by', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical MUO Container',
            },
        ),
    ]
