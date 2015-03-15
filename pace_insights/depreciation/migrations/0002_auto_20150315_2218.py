# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depreciation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='argument',
        ),
        migrations.RemoveField(
            model_name='job',
            name='result',
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(max_length=20, choices=[(b'start', b'start'), (b'running', b'running'), (b'finished', b'finished'), (b'failed', b'failed')]),
            preserve_default=True,
        ),
    ]
