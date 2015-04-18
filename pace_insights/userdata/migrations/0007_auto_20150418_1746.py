# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0006_auto_20150417_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='carmake_id',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='carmodel_id',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='carversion_id',
        ),
        migrations.AddField(
            model_name='userdata',
            name='carmake_name',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdata',
            name='carmodel_name',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdata',
            name='carversion_name',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userdata',
            name='depreciation',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
