# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0004_auto_20150415_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='depreciation_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
