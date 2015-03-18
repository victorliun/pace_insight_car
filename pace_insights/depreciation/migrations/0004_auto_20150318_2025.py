# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depreciation', '0003_auto_20150317_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='depreciation',
            name='year_0_mock',
            field=models.CharField(max_length=16, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='depreciation',
            name='year_1_mock',
            field=models.CharField(max_length=16, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='depreciation',
            name='year_2_mock',
            field=models.CharField(max_length=16, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='depreciation',
            name='year_3_mock',
            field=models.CharField(max_length=16, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='depreciation',
            name='year_4_mock',
            field=models.CharField(max_length=16, blank=True),
            preserve_default=True,
        ),
    ]
