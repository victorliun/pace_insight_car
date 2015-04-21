# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0007_auto_20150418_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='hp_loan_rate',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdata',
            name='loan_loan_rate',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdata',
            name='pcp_loan_rate',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
