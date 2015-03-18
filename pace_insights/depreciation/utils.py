# -*- coding: utf-8 -*-
'''
utils functions
'''
import random
import logging

logger = logging.getLogger(__file__)


def to_int(comma_int_str):
    '''Return int from comma int string'''
    if comma_int_str.startswith(u'£'):
        comma_int_str = comma_int_str[1:]
    try:
        return int(comma_int_str.replace(',', ''))
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
