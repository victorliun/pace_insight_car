# -*- coding: utf-8 -*-
"""
Test financial options.
"""
from __future__ import unicode_literals
from django.test import TestCase
from depreciation.financial_options import (
    HP, PCP, Lease, Loan
)
from depreciation.models import CarVersion

class FinancialOptionsTest(TestCase):
    """
    Test HP outputs
    """
    fixtures = ["financial_options"]

    def setUp(self):
        car_version = CarVersion.objects.all()[0]
        self.depreciation_id = car_version.depreciations.order_by(
            '-create_time')[0].id
    def test_hp(self):
        hp = HP(
            loan_at=0.07,
            term=4,
            stick_price=32485,
            deposit_amount=2580,
            depreciation_id=self.depreciation_id
        )
        self.assertEqual(hp.finance_value, 29905)
        self.assertEqual(hp.actual_monthly, 716.11)
        self.assertEqual(hp.equity_value, 15522)
        self.assertEqual(hp.effective_rate, 0.07)
        self.assertEqual(hp.total_payable(180), 35093.28)
        self.assertEqual(hp.value_score(180), 19571.28)
        self.assertEqual(hp.real_world_monthly(180), 407.73)

    def test_pcp(self):
        pcp = PCP(
            ballon_value=13970,
            loan_at=0.07,
            term=4,
            stick_price=32485,
            deposit_amount=2580,
            depreciation_id=self.depreciation_id
        )
        self.assertEqual(pcp.finance_value, 29905)
        self.assertEqual(pcp.equity_value, 15522)
        self.assertEqual(pcp.pure_equity_value(), 1552.0)
        self.assertEqual(pcp.actual_monthly, 463.08)
        self.assertEqual(pcp.total_payable(180), 25527.84)
        self.assertEqual(pcp.value_score(180), 23975.84)
        self.assertEqual(pcp.real_world_monthly(180), 499.5)

    def test_lease(self):
        lease = Lease(
            initial_payment=2150,
            term=2,
            monthly=209,
            extras=1500,
            actual_annual=8000,
            include=8000,
            price_per_mile=0.2,
            stick_price=32485,
            deposit_amount=2580,
            depreciation_id=self.depreciation_id
        )
        self.assertEqual(lease.finance_value, 29905)
        self.assertEqual(lease.actual_monthly, 313.30)
        self.assertEqual(lease.excess_mile_charges, 0)
        self.assertEqual(lease.effective_cost, 9785.90)
        self.assertEqual(lease.effective_monthly, 407.75)
        self.assertEqual(lease.total_payable(), 9785.90)
        self.assertEqual(lease.value_score(), 9785.90)


    def test_loan(self):
        loan = Loan(
            loan_at=0.039,
            term=4,
            stick_price=32485,
            deposit_amount=2580,
            loan_at_end=0,
            depreciation_id=self.depreciation_id
        )
        self.assertEqual(loan.finance_value, 29905)
        self.assertEqual(loan.actual_monthly, 673.89)
        self.assertEqual(loan.equity_value, 15522)
        self.assertEqual(loan.value_score(180), 17544.72)
        self.assertEqual(loan.real_world_monthly(180), 365.52)
        self.assertEqual(loan.total_payable(180), 33066.72)
