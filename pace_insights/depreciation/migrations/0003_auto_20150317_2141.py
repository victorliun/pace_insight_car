# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depreciation', '0002_auto_20150315_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarRoadTax',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('band', models.CharField(unique=True, max_length=8)),
                ('co2', models.CharField(max_length=64)),
                ('first_year_rate', models.CharField(max_length=64)),
                ('standard_rate', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(max_length=20, choices=[(b'scrapping', b'scrapping')]),
            preserve_default=True,
        ),
    ]
