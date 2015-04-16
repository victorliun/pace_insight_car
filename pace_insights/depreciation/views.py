"""
Views/Controllers
"""
import json

from django.http import JsonResponse
from django.shortcuts import render_to_response

from .financial_options import (
    HP, PCP, Lease, Loan
)
from .utils import parse_args
from userdata.utils import save_userdata


def home(request):
    return render_to_response('main.html')


def about(request):
    return render_to_response('about.html')


def graph_data_api(request):
    params = parse_args(request)
    data = {}
    data['values'] = []
    data['budget'] = params['monthly_budget']
    stick_price = params['list_price'] + params['extra_price']
    stick_price -= params['discount']
    term = params['term']
    px_amount = params['px_amount']
    deposit_amount = params['deposit_amount']
    depreciation_id = params['depreciation_id']
    tax = params['tax']
    if params.get('hp'):
        hp = HP(
            loan_at=params['hp_loan_rate'],
            term=params['hp_term'] or term,
            stick_price=stick_price,
            px_amount=px_amount,
            deposit_amount=deposit_amount,
            depreciation_id=depreciation_id
        )
        hp_result = {
            'True monthly cost': int(
                round(hp.real_world_monthly(tax))),
            'Regular monthly payment': int(round(hp.actual_monthly)),
            'financial_option': 'HP',
            "Total Cost for Comparison" : int(round(hp.value_score(tax)))
        }
        data['values'].append(hp_result)

    if params.get('pcp'):
        pcp = PCP(
            ballon_value=params['pcp_ballon_value'],
            loan_at=params['pcp_loan_rate'],
            term=params['pcp_term'] or term,
            stick_price=stick_price,
            px_amount=px_amount,
            deposit_amount=deposit_amount,
            depreciation_id=depreciation_id
        )
        pcp_result = {
            'True monthly cost': int(
                round(pcp.real_world_monthly(tax))),
            'Regular monthly payment': int(round(pcp.actual_monthly)),
            'financial_option': 'PCP',
            "Total Cost for Comparison" : int(round(pcp.value_score(tax)))
        }
        data['values'].append(pcp_result)

    if params.get('lease'):
        lease = Lease(
            initial_payment=params['lease_initial_payment'],
            monthly=params['lease_monthly_payment'],
            extras=params['lease_extras'],
            term=params['lease_term'] or term,
            stick_price=stick_price,
            actual_annual=params['lease_predicted_mileage'],
            include=params['lease_included_mileage'],
            price_per_mile=params['lease_excess_mile_price'],
            px_amount=px_amount,
            deposit_amount=deposit_amount,
            depreciation_id=depreciation_id
        )
        lease_result = {
            'True monthly cost': int(
                round(lease.effective_monthly)),
            'Regular monthly payment': int(round(lease.actual_monthly)),
            'financial_option': 'LEASE',
            "Total Cost for Comparison" : int(round(lease.value_score()))
        }
        data['values'].append(lease_result)

    if params.get('loan'):
        loan = Loan(
            loan_at=params['loan_loan_rate'],
            term=params['term'] or term,
            loan_at_end=params['loan_loan_at_end'],
            stick_price=stick_price,
            px_amount=px_amount,
            deposit_amount=deposit_amount,
            depreciation_id=depreciation_id
        )
        loan_result = {
            'True monthly cost': int(
                round(loan.real_world_monthly(tax))),
            'Regular monthly payment': int(round(loan.actual_monthly)),
            'financial_option': 'LOAN',
            "Total Cost for Comparison" : int(round(loan.value_score(tax)))
        }
        data['values'].append(loan_result)

    print data
    ddata = {
    'budget': 300,
    'values': [
        {
            'True monthly cost': 408, 
            'Regular monthly payment': 716,
            "Total Cost for Comparison" : 1000,
            'financial_option': 'HP',
        },
        {
            'True monthly cost': 500, 
            'Regular monthly payment': 463,
            'financial_option': 'PCP',
        },
        {
            'True monthly cost': 408, 
            'Regular monthly payment': 313,
            'financial_option': 'LEASE',
        },
        {
            'True monthly cost': 336, 
            'Regular monthly payment': 674,
            'financial_option': 'LOAN',
        },
    ]}
    sorted_values = sorted(data['values'], key=lambda x:x['True monthly cost'])
    data['values'] = sorted_values
    save_userdata(params)
    return JsonResponse(data)