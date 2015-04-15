# -*- coding: utf-8 -*-
'''
utils functions
'''
from __future__ import unicode_literals
import random
import logging
import json
import geocoder
from ipware.ip import get_ip

logger = logging.getLogger(__file__)


class Price(object):
    '''Price object.
    @amount: how much
    @currency: currency
    '''
    def __init__(self, amount, currency=u'£'):
        self.amount = amount
        self.currency = currency

    @classmethod
    def fromstring(cls, price):
        ''' comma separated price(string) starts by currency.
        e.g.:
            "£12,345" or '£12345'
        '''
        return cls(to_int(price), price[0])

    def __str__(self):
        return u'{}{}'.format(
            self.currency,
            int_to_str(self.amount)
        )

    def __add__(self, other):
        if self.currency != other.currency:
            raise Exception(
                u'Trying to add {} to {}',format(
                    self.currency,
                    other.currency)
            )
        else:
            return Price(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        if self.currency != other.currency:
            raise Exception(
                u'Trying to sub {} to {}',format(
                    self.currency,
                    other.currency)
            )
        else:
            return Price(self.amount - other.amount, self.currency)

    def __mul__(self, percentage):
        amount = int(round(self.amount * percentage))
        return Price(amount, self.currency)

    def __div__(self, price):
        amount = self.amount * 1.00
        if isinstance(price, Price):
            return round(amount / price.amount, 8)
        else:
            amount = int(round(amount / price))
            return Price(amount, self.currency)

    def __eq__(self, other):
        return self.currency == other.currency and self.amount == other.amount


class DepreciationProfile(object):
    '''
    This depreciation profile contain initial price and 4 years depreciation.
    '''
    def __init__(self, depr_list, start_price):
        self.depr_list = map(lambda x: Price.fromstring(x), depr_list)
        self.start_price = Price.fromstring(start_price)

    @property
    def exact_depreciations(self):
        """
        include four years depreciation prices
        """
        new_trend = [self.start_price,]
        for index, depr in enumerate(self.depr_list[:-1]):
            percentage = self.depr_list[index + 1] / self.depr_list[index]
            new_price = new_trend[index] * percentage
            new_trend.append(new_price)

        return new_trend

    @property
    def cost_per_year(self):
        '''Yearly cost.'''
        cost_per_year = [Price(0)]

        for year in xrange(1,5):
            last_year = self.exact_depreciations[year - 1]
            cost_per_year.append(
                last_year - self.exact_depreciations[year])

        return cost_per_year

    @property
    def running_total(self):
        '''Yearly cost sum up'''

        start = self.cost_per_year[1]
        total_cost = [Price(0), start]
        for cost in self.cost_per_year[2:]:
            start += cost
            total_cost.append(start)

        return total_cost

    @property
    def monthly_cost(self):
        '''divide running_total by 12'''
        return [cost / 12 for cost in self.cost_per_year]


def to_int(comma_int_str):
    '''Return int from comma int string'''
    if comma_int_str.startswith(u'£'):
        comma_int_str = comma_int_str[1:]
    try:
        comma_int_str = comma_int_str.replace(',', '')
        if '.' in comma_int_str:
            return_val = int(round(float(comma_int_str)))
        else:
            return_val = int(comma_int_str)
        return return_val
    except ValueError, err:
        logger.error(err)
        return 0


def random50():
    '''return a random value(int) between -50 to +50'''
    return random.randint(-50,50)


def make_new_depreciation(old_depr):
    '''This function will return a new depreciation based on
    the old one. 
    '''
    currency = old_depr[0]
    old_data = to_int(old_depr)
    new_data = old_data + random50()

    new_depr = currency + int_to_str(new_data)
    return new_depr


def int_to_str(int_number, separator=','):
    '''Return comma separated string'''
    int_number_str = list(str(int_number))
    int_number_str.reverse()
    
    result = []
    for index, num in enumerate(int_number_str):
        result.insert(0, num)
        if (index + 1) % 3 == 0 and index != len(int_number_str) - 1:
            result.insert(0, separator)

    return ''.join(result)


def parse_args(request):
    """
    Parse args from request, return dict.
    """

    comp_form = dict(zip(
        request.GET.keys(),
        request.GET.values()))
    params = {}

    params['browser_type'] = request.META['HTTP_USER_AGENT']
    ip = get_ip(request)
    params['ip_addr'] = ip
    geo = geocoder.ip(ip)
    params['location'] = geo.city
    params['country'] = geo.country

    params['monthly_budget'] = int(comp_form['monthlyBudget'])
    params['discount'] = int(comp_form.get('discount', 0))
    params['list_price'] = int(comp_form['totalPrice'])
    params['extra_price'] = int(comp_form.get('extraPrice', 0))
    params['depreciation_id'] = int(comp_form['depreciationId'])
    params['tax'] = int(comp_form['tax'])

    params['px_amount'] = int(comp_form.get('pxAmount', 0))
    params['deposit_amount'] = int(comp_form.get('depositAmount', 0))

    params['term'] = int(comp_form['term'])
    if comp_form.get('foHP') == 'True':
        hp_data = json.loads(comp_form.get('hp').decode('cp1252'))
        params['hp'] = True
        params['hp_term'] = hp_data.get('term', 0)
        params['hp_loan_rate'] = hp_data['loan_at'] / 100.0

    if comp_form.get('foPCP') == 'True':
        pcp_data = json.loads(comp_form.get('pcp').decode('cp1252'))
        params['pcp'] = True
        params['pcp_term'] = pcp_data.get('term', 0)
        params['pcp_loan_rate'] = pcp_data['loan_at'] / 100.0
        params['pcp_ballon_value'] = pcp_data['ballon_value']

    if comp_form.get('foLease') == 'True':
        lease_data = json.loads(comp_form.get('lease').decode('cp1252'))
        params['lease'] = True
        params['lease_term'] = lease_data.get('term')
        params['lease_extras'] = lease_data.get('extras', 0)
        params['lease_initial_payment'] = lease_data['initial_payment']
        params['lease_monthly_payment'] = lease_data['monthly']
        params['lease_predicted_mileage'] = lease_data.get('actual_annual', 0)
        params['lease_included_mileage'] = lease_data.get('include_mileages', 0)
        params['lease_excess_mile_price'] = lease_data.get('price_per_mile', 0)

    if comp_form.get('foLoan') == 'True':
        loan_data = json.loads(comp_form.get('loan').decode('cp1252'))
        params['loan'] = True
        params['loan_term'] = loan_data.get('term', 0)
        params['loan_loan_rate'] = loan_data['loan_at'] / 100.0
        params['loan_loan_at_end'] = loan_data.get('loan_at_end',0)

    return params
