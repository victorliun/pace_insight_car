# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_auto_20150415_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='city',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdata',
            name='country',
            field=models.CharField(max_length=255, null=True),
            preserve_default=True,
        ),
    ]
