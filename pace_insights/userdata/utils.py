# -*- coding: utf-8 -*-
'''
utils functions for userdata
'''
from __future__ import unicode_literals
import logging

from .models import UserData

logger = logging.getLogger(__file__)


def save_userdata(params):
    """Params includes all the data for userdata.
    """
    userdata = UserData()
    userdata.list_price = params['list_price']
    userdata.extra_price = params['extra_price']
    userdata.discount = params['discount']
    userdata.deposit_amount = params['deposit_amount']
    userdata.px_amount = params['px_amount']
    userdata.term = params['term']
    userdata.monthly_budget = params['monthly_budget']
    userdata.road_tax = params['tax']

    # hp options
    if params.get('hp'):
        userdata.hp = params['hp']
        userdata.hp_term = params['hp_term']
        userdata.hp_loan_rate = params['hp_loan_rate']

    # pcp options
    if params.get('pcp'):
        userdata.pcp = params['pcp']
        userdata.pcp_term = params['pcp_term']
        userdata.pcp_loan_rate = params['pcp_loan_rate']
        userdata.pcp_ballon_value = params['pcp_ballon_value']
    
    # lease options
    if params.get('lease'):
        userdata.lease = params['lease']
        userdata.lease_term = params['lease_term']
        userdata.lease_extra = params['lease_extra']
        userdata.lease_initial_payment = params['lease_initial_payment']
        userdata.lease_monthly_payment = params['lease_monthly_payment']
        userdata.lease_predicted_mileage = params['lease_predicted_mileage']
        userdata.lease_included_mileage = params['lease_included_mileage']
        userdata.lease_excess_mile_price = params['lease_excess_mile_price']

    # loan options
    if params.get('loan'):
        userdata.loan = params['loan']
        userdata.loan_term = params['loan_term']
        userdata.loan_loan_rate = params['loan_loan_rate']
        userdata.loan_loan_at_end = params['loan_loan_at_end']

    # general data
    userdata.browser_type = params['browser_type']
    userdata.ip_addr = params['ip_addr']
    userdata.city = params['city']
    userdata.country = params['country']
    userdata.save()

    print userdata

