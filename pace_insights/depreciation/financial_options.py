# -*- coding: utf-8 -*-
"""
Depreciation App: financial options
"""
from __future__ import unicode_literals
import numpy
import logging

from depreciation.utils import Price, DepreciationProfile, int_to_str

logger = logging.getLogger(__name__)


class FinancailOption(object):
    """This the subclass of"""

    def __init__(self, loan_at=0.1, stick_price=0,
        total_up_front=0, term=4, car_version=None, loan_at_end=0):
        self.loan_at = loan_at
        self.total_months = term * 12
        self.total_up_front = total_up_front
        self.finance_value = stick_price - total_up_front
        self.loan_at_end = loan_at_end

        if car_version is None:
            raise Exception('Invalid car version')
        depreciation = car_version.depreciations.order_by(
            '-create_time')[0]
        depr_profile = DepreciationProfile(
            depreciation.get_raw_data(),
            int_to_str(self.finance_value)
        )

        last_depr = depr_profile.exact_depreciations[-1]
        self.last_depr = last_depr.amount

    @property
    def actual_monthly(self):
        """User actually paid monthly money for the car."""
        actual_monthly = numpy.pmt(
            self.loan_at / 12,
            self.total_months,
            self.finance_value,
            self.loan_at_end
        )
        logger.info('numpy.pmt({},{},{},{})={}'.format(
            self.loan_at / 12,
            self.total_months,
            self.finance_value,
            self.loan_at_end,
            actual_monthly
        ))
        return int(round(actual_monthly))

    @property
    def equity_value(self):
        return self.loan_at_end + self.last_depr

    @property
    def effective_rate(self):
        # TODO: Recalculate effective rate.
        return self.loan_at

    def total_payable(self, tax_per_year=0):
        '''
        '''
        payment = self.actual_monthly * self.total_months
        return payment + tax_per_year * self.total_months / 12

    def value_score(self, tax_per_year=0):
        out_of_pocket = self.total_payable(tax_per_year) - self.equity_value

        return out_of_pocket

    def real_world_monthly(self, tax_per_year=0):
        """Real world out of pocket money for this car.
        This will show real value of buying the car.
        """

        return self.value_score(tax_per_year) / self.total_months


class HP(FinancailOption):
     name = 'HP'


class PCP(FinancailOption):
    name = 'PCP'

    def __init__(self, ballon_value=0, *args, **kwargs):
        self.ballon_value = ballon_value
        super(PCP, self).__init__(*args, **kwargs)

    def ballon_est(self):
        self.ballon_est = int(round(self.ballon_value * self.equity_value))

    def equity_value(self):
        return self.last_depr - self.ballon_est

    def total_payable(self, tax_per_year=0):
        '''
        '''
        finance = self.actual_monthly * self.total_months
        tax = tax_per_year * self.total_months / 12

        return self.total_up_front + finance + tax


class Loan(FinancailOption):
    name = "Loan"


VAT = 1.2
class Lease(FinancailOption):
    name = 'Lease'

    def __init__(self, initial_payment, monthly, extras, *args, **kwargs):
        super(Lease, self).__init__(*args, **kwargs)
        self.initial_payment = int(round(initial_payment * VAT))
        self.monthly = int(round(monthly * VAT))
        self.monthly_extras = extras / self.total_months

    @property
    def actual_monthly(self):
        return self.monthly + self.monthly_extras

    def exess_mile_charges(self, actual_annual=8000,
            include=8000, price_per_mile=0.20):
        # price per mile include VAT
        excess = actual_annual - include
        return excess * price_per_mile

    @property
    def effective_cost(self):
        return self.initial_payment + self.actual_monthly * (
            self.total_months - 1)
        

    @property
    def effective_monthly(self):
        return self.effective_cost / self.total_months


    def total_payable(self):
        return self.effective_cost

    def value_score(self, px=0):
        return self.effective_cost + px

 
