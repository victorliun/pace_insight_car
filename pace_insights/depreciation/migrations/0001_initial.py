# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('whatcar_id', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Car Makes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('whatcar_id', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('car_make', models.ForeignKey(related_name='car_models', to='depreciation.CarMake')),
            ],
            options={
                'verbose_name_plural': 'Car Models',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CarVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('whatcar_id', models.IntegerField(default=0)),
                ('doors', models.IntegerField(default=0)),
                ('body_range', models.CharField(max_length=64, null=True)),
                ('create_time', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('car_model', models.ForeignKey(related_name='car_versions', to='depreciation.CarModel')),
            ],
            options={
                'verbose_name_plural': 'Car Versions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Depreciation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('year_0', models.CharField(max_length=16)),
                ('year_1', models.CharField(max_length=16)),
                ('year_2', models.CharField(max_length=16)),
                ('year_3', models.CharField(max_length=16)),
                ('year_4', models.CharField(max_length=16)),
                ('car_version', models.ForeignKey(related_name='depreciations', to='depreciation.CarVersion')),
            ],
            options={
                'get_latest_by': 'create_time',
                'verbose_name_plural': 'Depreciations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FinancialOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('create_time', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_type', models.CharField(max_length=20, choices=[(b'fibonacci', b'fibonacci'), (b'power', b'power')])),
                ('status', models.CharField(max_length=20, choices=[(b'pending', b'pending'), (b'started', b'started'), (b'finished', b'finished'), (b'failed', b'failed')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('argument', models.PositiveIntegerField()),
                ('result', models.IntegerField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='carversion',
            unique_together=set([('name', 'car_model')]),
        ),
        migrations.AlterUniqueTogether(
            name='carmodel',
            unique_together=set([('name', 'car_make')]),
        ),
    ]
