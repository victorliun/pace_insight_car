# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depreciation', '0004_auto_20150318_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmake',
            options={'ordering': ('name',), 'verbose_name_plural': 'Car Makes'},
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ('name',), 'verbose_name_plural': 'Car Models'},
        ),
        migrations.AlterModelOptions(
            name='carversion',
            options={'ordering': ('name',), 'verbose_name_plural': 'Car Versions'},
        ),
        migrations.AlterModelOptions(
            name='depreciation',
            options={'ordering': ['-create_time'], 'get_latest_by': 'create_time', 'verbose_name_plural': 'Depreciations'},
        ),
    ]
