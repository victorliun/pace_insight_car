# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0002_auto_20150415_2001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='brower_type',
            new_name='browser_type',
        ),
    ]
