# -*- coding: utf-8 -*-
'''
Models for depreciation.
'''
import logging
import json
from datetime import datetime

from django.db import models
from user_agents import parse
from depreciation.models import Depreciation
from depreciation.utils import to_int

class UserData(models.Model):
    """
    Model for capture UserData
    """
    list_price = models.IntegerField(default=0)
    extra_price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    deposit_amount = models.IntegerField(null=True)
    px_amount = models.IntegerField(null=True)
    term = models.IntegerField(default=1)
    monthly_budget = models.IntegerField(default=0)
    road_tax = models.IntegerField(default=0)
    depreciation_id = models.IntegerField(default=0)
    carmake_name = models.CharField(max_length=255, blank=True, null=True)
    carversion_name = models.CharField(max_length=255, blank=True, null=True)
    carmodel_name = models.CharField(max_length=255, blank=True, null=True)
    depreciation = models.CharField(max_length=255, blank=True, null=True)

    # hp options
    hp = models.BooleanField(default=False)
    hp_term = models.IntegerField(null=True)
    hp_loan_rate = models.IntegerField()

    # pcp options
    pcp = models.BooleanField(default=False)
    pcp_term = models.IntegerField(null=True)
    pcp_loan_rate = models.IntegerField(null=True)
    pcp_ballon_value = models.IntegerField(null=True)
    
    # lease options
    lease = models.BooleanField(default=False)
    lease_term = models.IntegerField(null=True)
    lease_extra = models.IntegerField(null=True)
    lease_initial_payment = models.IntegerField(null=True)
    lease_monthly_payment = models.IntegerField(null=True)
    lease_predicted_mileage = models.IntegerField(null=True)
    lease_included_mileage = models.IntegerField(null=True)
    lease_excess_mile_price = models.IntegerField(null=True)

    # loan options
    loan = models.BooleanField(default=False)
    loan_term = models.IntegerField(null=True)
    loan_loan_rate = models.IntegerField(null=True)
    loan_loan_at_end = models.IntegerField(null=True)

    # general data
    browser_type = models.CharField(max_length=255)
    ip_addr = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    create_time = models.DateTimeField(auto_now_add=True, auto_now=True)

    @property
    def user_agent(self):
        return parse(self.browser_type)

    def save(self, *args, **kwargs):
        depreciation = Depreciation.objects.get(pk=self.depreciation_id)
        self.depreciation = json.dumps([
           to_int(price) for price in depreciation.get_addon_data()])
        self.carversion_name = depreciation.car_version.name
        self.carmodel_name = depreciation.car_version.car_model.name
        self.carmake_name = depreciation.car_version.car_model.car_make.name
        return super(UserData, self).save(*args, **kwargs)
