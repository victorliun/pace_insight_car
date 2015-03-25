# -*- coding: utf-8 -*-
'''
utils functions
'''
from __future__ import unicode_literals
import random
import logging

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
