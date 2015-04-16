# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list_price', models.IntegerField(default=0)),
                ('extra_price', models.IntegerField(null=True)),
                ('discount', models.IntegerField(null=True)),
                ('deposit_amount', models.IntegerField(null=True)),
                ('px_amount', models.IntegerField(null=True)),
                ('term', models.IntegerField(default=1)),
                ('monthly_budget', models.IntegerField(default=0)),
                ('road_tax', models.IntegerField(default=0)),
                ('hp', models.BooleanField(default=False)),
                ('hp_term', models.IntegerField(null=True)),
                ('hp_loan_rate', models.IntegerField()),
                ('pcp', models.BooleanField(default=False)),
                ('pcp_term', models.IntegerField(null=True)),
                ('pcp_loan_rate', models.IntegerField(null=True)),
                ('pcp_ballon_value', models.IntegerField(null=True)),
                ('lease', models.BooleanField(default=False)),
                ('lease_term', models.IntegerField(null=True)),
                ('lease_extra', models.IntegerField(null=True)),
                ('lease_initial_payment', models.IntegerField(null=True)),
                ('lease_monthly_payment', models.IntegerField(null=True)),
                ('lease_predicted_mileage', models.IntegerField(null=True)),
                ('lease_included_mileage', models.IntegerField(null=True)),
                ('lease_excess_mile_price', models.IntegerField(null=True)),
                ('loan', models.BooleanField(default=False)),
                ('loan_term', models.IntegerField(null=True)),
                ('loan_loan_rate', models.IntegerField(null=True)),
                ('loan_loan_at_end', models.IntegerField(null=True)),
                ('browers_type', models.CharField(max_length=255)),
                ('ip_addr', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
