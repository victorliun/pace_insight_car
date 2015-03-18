# -*- coding: utf-8 -*-
"""
Depreciation App: tests
"""
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
