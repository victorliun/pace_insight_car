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
        self.car_version = CarVersion.objects.all()[0]
        print self.car_version

    def test_hp(self):
        hp = HP(
            loan_at=0.07,
            term=4,
            stick_price=32485,
            total_up_front=2580,
            car_version=self.car_version
        )
        self.assertEqual(self.finance_value, 29905)
        self.assertEqual(hp.actual_monthly, 716)
        self.assertEqual(hp.equity_value, 15522)
        self.assertEqual(hp.effective_rate, 0.07)
        self.assertEqual(hp.value_score(180), 19572)
        self.assertEqual(hp.real_world_monthly(180), 408)
        self.assertEqual(hp.total_payable(180), 35094)

    def test_pcp(self):
        hp = PCP(
            ballon_value=0.9,
            loan_at=0.07,
            term=4,
            stick_price=32485,
            total_up_front=2580,
            car_version=self.car_version
        )
        self.assertEqual(self.finance_value, 29905)
        self.assertEqual(hp.actual_monthly, 463)
        self.assertEqual(hp.equity_value, 1552)
        self.assertEqual(hp.value_score(180), 23967)
        self.assertEqual(hp.real_world_monthly(180), 500)
        self.assertEqual(hp.total_payable(180), 15528)

    def test_lease(self):
        hp = Lease(
            initial_payment=2150,
            term=2,
            monthly=209,
            extras=1500,
            stick_price=32485,
            total_up_front=2580,
            car_version=self.car_version
        )
        self.assertEqual(self.finance_value, 29905)
        self.assertEqual(hp.actual_monthly, 408)
        self.assertEqual(hp.excess_mile_charges(
            actual_annual=8000,
            include=8000), 0)
        self.assertEqual(hp.effective_cost, 9786)
        self.assertEqual(hp.effective_monthly, 408)
        self.assertEqual(hp.total_payable(), 9786)
        self.assertEqual(hp.value_score(200), 9986)


    def test_loan(self):
        hp = PCP(
            loan_at=0.039,
            term=4,
            stick_price=32485,
            total_up_front=2580,
            loan_at_end=0,
            car_version=self.car_version
        )
        self.assertEqual(self.finance_value, 29905)
        self.assertEqual(hp.actual_monthly, 674)
        self.assertEqual(hp.equity_value, 1552)
        self.assertEqual(hp.value_score(180), 17545)
        self.assertEqual(hp.real_world_monthly(180), 366)
        self.assertEqual(hp.total_payable(180), 720)
