# -*- coding: utf-8 -*-
'''
Models for depreciation.
'''
import logging
from datetime import datetime

from django.db import models


class UserData(models.Model):
    """
    Model for capture UserData
    """
    list_price = models.IntegerField()
    extra_price = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    deposit_amount = models.IntegerField(null=True)
    part_exchange_amount = models.IntegerField(null=True)
    term = models.IntegerField()
    target_monthly_budget = models.IntegerField()
    road_tax = models.IntegerField()

    # hp options
    hp_term = models.IntegerField(null=True)
    hp_loan_rate = models.IntegerField()

    # pcp options
    pcp_term = models.IntegerField(null=True)
    pcp_loan_rate = models.IntegerField()
    pcp_est_ballon_value = models.IntegerField()
    
    # lease options
    lease_term = models.IntegerField(null=True)
    lease_extra = models.IntegerField(null=True)
    lease_initial_payment = models.IntegerField()
    lease_monthly_payment = models.IntegerField()
    lease_predicted_mileage = models.IntegerField(null=True)
    lease_included_mileage = models.IntegerField(null=True)
    lease_excess_mile_price = models.IntegerField(null=True)

    # loan options
    loan_term = models.IntegerField(null=True)
    loan_loan_rate = models.IntegerField()
    loan_loan_at_end = models.IntegerField(null=True)

    # general data
    browers_type = models.CharField(max_length=255)
    ip_addr = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True, auto_now=True)
