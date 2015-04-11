# -*- coding: utf-8 -*-
"""
Depreciation App: financial options
"""
from __future__ import unicode_literals
import numpy
import logging

from depreciation.utils import Price, DepreciationProfile, int_to_str
from depreciation.models import Depreciation


logger = logging.getLogger(__name__)


class FinancailOption(object):
    """This the subclass of"""

    def __init__(self, loan_at=0.1, stick_price=0,
            deposit_amount=0, px_amount=0, term=4,
            depreciation_id=None, loan_at_end=0):
        # print loan_at, loan_at_end, depreciation_id, deposit_amount, term, stick_price
        self.loan_at = loan_at
        self.total_months = term * 12
        self.total_up_front = deposit_amount + px_amount
        self.px_amount = px_amount
        self.finance_value = stick_price - self.total_up_front
        self.loan_at_end = loan_at_end

        if depreciation_id is None:
            raise Exception('Invalid car version')
        depreciation = Depreciation.objects.get(pk=depreciation_id)
        depr_profile = DepreciationProfile(
            depreciation.get_raw_data(),
            int_to_str(stick_price)
        )
        last_depr = depr_profile.exact_depreciations[-1]
        self.last_depr = last_depr.amount

    @property
    def actual_monthly(self):
        """User actually paid monthly money for the car."""
        actual_monthly = numpy.pmt(
            self.loan_at / 12,
            self.total_months,
            -self.finance_value,
            self.loan_at_end
        )
        logger.info('numpy.pmt({},{},{},{})={}'.format(
            self.loan_at / 12,
            self.total_months,
            -self.finance_value,
            self.loan_at_end,
            actual_monthly
        ))
        return round(actual_monthly, 2)

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
        real_world_pay = self.value_score(tax_per_year) / self.total_months
        return round(real_world_pay, 2)


class HP(FinancailOption):
     name = 'HP'


class PCP(FinancailOption):
    name = 'PCP'

    def __init__(self, ballon_value=0, *args, **kwargs):
        self.ballon_value = ballon_value
        super(PCP, self).__init__(*args, **kwargs)
        self.loan_at_end = ballon_value

    @property
    def equity_value(self):
        return self.last_depr

    def pure_equity_value(self):
        pev = round(self.equity_value - self.ballon_value, 2)
        return pev

    def total_payable(self, tax_per_year=0):
        '''
        Total money to pay.
        '''
        finance = self.actual_monthly * self.total_months
        tax = tax_per_year * self.total_months / 12

        return self.total_up_front + finance + tax

    def value_score(self, tax_per_year=0):
        return self.total_payable(tax_per_year) - self.pure_equity_value()


class Loan(FinancailOption):
    name = "Loan"


VAT = 1.2
class Lease(FinancailOption):
    name = 'Lease'

    def __init__(self, initial_payment, monthly, extras,
            actual_annual=0, include=0, price_per_mile=0.20, *args, **kwargs):
        super(Lease, self).__init__(*args, **kwargs)
        self.initial_payment = round(initial_payment * VAT, 2)
        self.monthly = round(monthly * VAT, 2)
        self.monthly_extras = round(extras * 1.0 / self.total_months, 2)
        self.actual_annual = actual_annual
        self.include = include
        self.price_per_mile = price_per_mile

    @property
    def actual_monthly(self):
        return self.monthly + self.monthly_extras

    @property
    def excess_mile_charges(self):
        # price per mile include VAT
        excess = self.actual_annual - self.include
        return excess * self.price_per_mile * self.total_months / 12

    @property
    def effective_cost(self):
        total_instalment = round(self.actual_monthly * (
            self.total_months - 1), 2)
        cost = self.initial_payment + total_instalment 
        cost += self.excess_mile_charges
        return cost

    @property
    def effective_monthly(self):
        return round(self.value_score() / self.total_months, 2)


    def total_payable(self):
        return self.effective_cost

    def value_score(self):
        return self.effective_cost - self.px_amount
