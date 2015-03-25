# -*- coding: utf-8 -*-
"""
Depreciation App: tests
"""
from __future__ import unicode_literals
from django.test import TestCase
from depreciation import utils

class UtilsTest(TestCase):
    """
    Test every utils in utils.py
    """

    def test_to_int(self):
        self.assertEqual(utils.to_int(u'£123,456'), 123456)

    def test_random50(self):
        for index in range(10):
            self.assertTrue(
                utils.random50() <= 50 and utils.random50() >= -50)

    def test_int_to_str(self):
        self.assertEqual(utils.int_to_str(123456), '123,456')

    def test_make_new_depreciation(self):
        new = utils.make_new_depreciation(u'£123,456')
        new = utils.to_int(new)
        old = utils.to_int(u'£123,456')
        self.assertTrue(
            new >= old - 50 and new <= old + 50
        )

    def test_price_add(self):
        p1 = utils.Price.fromstring(u'£123,456')
        p2 = utils.Price(1)
        self.assertEqual(p1 + p2, utils.Price.fromstring(u'£123,457'))

    def test_price_sub(self):
        p1 = utils.Price.fromstring(u'£123,456')
        p2 = utils.Price(1)
        self.assertEqual(p1 - p2, utils.Price.fromstring(u'£123,455'))

    def test_price_mul(self):
        p1 = utils.Price.fromstring(u'£123,456')
        new_p1 = p1 * 0.1
        self.assertEqual(new_p1, utils.Price.fromstring(u'£12,346'))

    def test_price_div_1(self):
        p1 = utils.Price.fromstring(u'£123,456')
        new_p1 = p1 / 2
        self.assertEqual(new_p1, utils.Price.fromstring(u'£61,728'))

    def test_price_div_2(self):
        p1 = utils.Price.fromstring(u'£123,456')
        p2 = utils.Price.fromstring(u'£123,000')
        expect_result = round(p1.amount * 1.0 / p2.amount, 8)
        self.assertEqual(p1 / p2, expect_result)


class DepreciationProfileTest(TestCase):
    """Test depreciation profile functions."""
    def setUp(self):
        deprecs = ['£30,805', '£25,559', '£21,021', '£17,238', '£14,719']
        start_price = '£32,485'
        self.dp = utils.DepreciationProfile(deprecs, start_price)

    def test_exact_depreciations(self):
        desire_output = ['£32,485', '£26,953', '£22,167', '£18,178', '£15,522']
        output_price = map(lambda x: utils.Price.fromstring(x), desire_output)
        exact_output = self.dp.exact_depreciations
        self.assertEqual(
            output_price, exact_output
        )
    
    def test_cost_per_year(self):
        desire_output = ['£0', '£5,532', '£4,786', '£3,989', '£2,656']
        output_price =map(
            lambda x: utils.Price.fromstring(x),
            desire_output)
        exact_output = self.dp.cost_per_year
        self.assertEqual(
            output_price, exact_output
        )

    def test_running_total(self):
        desire_output = ['£0', '£5,532', '£10,318', '£14,307', '£16,963']
        output_price = map(
            lambda x: utils.Price.fromstring(x),
            desire_output)
        exact_output = self.dp.running_total
        self.assertEqual(
            output_price, exact_output
        )

    def test_monthly_cost(self):
        desire_output = ['£0', '£461.01', '£398.80', '£332.45', '£221.37']
        output_price = map(
            lambda x: utils.Price.fromstring(x),
            desire_output)
        exact_output = self.dp.monthly_cost
        self.assertEqual(
            output_price, exact_output
        )
