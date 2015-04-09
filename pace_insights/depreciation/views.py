"""
Views/Controllers
"""
import json

from django.http import JsonResponse
from django.shortcuts import render_to_response

from .financial_options import (
    HP, PCP, Lease, Loan
)

def home(request):
    return render_to_response('main.html')


def about(request):
    return render_to_response('about.html')


def graph_data_api(request):
    comp_form = dict(zip(
        request.GET.keys(),
        request.GET.values()))
    data = {}
    data['budget'] = int(comp_form['monthlyBudget'])
    data['values'] = []
    discount = float(comp_form.get('discount', 0))
    total_price = int(comp_form['totalPrice'])
    extra_price = int(comp_form.get('extraPrice', 0))
    depreciation_id = int(comp_form['depreciationId'])
    tax = int(comp_form['tax'])
    stick_price = (total_price + extra_price) * (1 - discount / 100.0)

    px_amount = int(comp_form.get('pxAmount', 0))
    deposit_amount = int(comp_form.get('depositAmount', 0))
    if comp_form.get('foHP') == 'True':
        hp_data = json.loads(comp_form.get('hp').decode('cp1252'))
        loan_at = hp_data['loan_at'] / 100.0
        loan_at_end = hp_data.get('loan_at_end', 0)
        hp = HP(
            loan_at=loan_at,
            loan_at_end=loan_at_end,
            term=hp_data['term'],
            stick_price=int(stick_price),
            px_amount=px_amount,
            deposit_amount=deposit_amount,
            depreciation_id=depreciation_id
        )
        hp_result = {
            'True monthly cost': int(
                round(hp.real_world_monthly(tax))),
            'Regular monthly payment': int(round(hp.actual_monthly)),
            'financial_option': 'HP',
        }
        data['values'].append(hp_result)

    if comp_form.get('foPCP') == 'True':
        pcp_data = json.loads(comp_form.get('pcp').decode('cp1252'))
        loan_at = pcp_data['loan_at'] / 100.0
        ballon_value = pcp_data['ballon_value'] / 100.0

        pcp = PCP(
            ballon_value=ballon_value,
            loan_at=loan_at,
            term=pcp_data['term'],
            stick_price=int(stick_price),
            px_amount=px_amount,
            deposit_amount=deposit_amount,
            depreciation_id=depreciation_id
        )
        pcp.set_loan_at_end(pcp.ballon_est)
        pcp_result = {
            'True monthly cost': int(
                round(pcp.real_world_monthly(tax))),
            'Regular monthly payment': int(round(pcp.actual_monthly)),
            'financial_option': 'PCP',
        }
        data['values'].append(pcp_result)

    if comp_form.get('foLease') == 'True':
        lease_data = json.loads(comp_form.get('lease').decode('cp1252'))
        monthly = lease_data['monthly']
        initial_payment = lease_data['initial_payment']
        extras = lease_data['extras']
        actual_annual = lease_data.get('actual_annual', 0)
        include_mileages = lease_data.get('include_mileages', 0)
        price_per_mile = lease_data.get('price_per_mile', 0)
        lease = Lease(
            initial_payment=initial_payment,
            monthly=monthly,
            extras=extras,
            term=lease_data['term'],
            stick_price=int(stick_price),
            actual_annual=actual_annual,
            include=include_mileages,
            price_per_mile=price_per_mile,
            px_amount=px_amount,
            deposit_amount=deposit_amount,
            depreciation_id=depreciation_id
        )
        lease_result = {
            'True monthly cost': int(
                round(lease.effective_monthly)),
            'Regular monthly payment': int(round(lease.actual_monthly)),
            'financial_option': 'LEASE',
        }
        data['values'].append(lease_result)
    
    if comp_form.get('foLoan') == 'True':
        loan_data = json.loads(comp_form.get('loan').decode('cp1252'))
        loan_at = loan_data['loan_at'] / 100
        loan_at_end = loan_data.get('loan_at_end',0)
        loan = Loan(
            loan_at=loan_at,
            term=loan_data['term'],
            loan_at_end=loan_at_end,
            stick_price=int(stick_price),
            px_amount=px_amount,
            deposit_amount=deposit_amount,
            depreciation_id=depreciation_id
        )
        loan_result = {
            'True monthly cost': int(
                round(loan.real_world_monthly(tax))),
            'Regular monthly payment': int(round(loan.actual_monthly)),
            'financial_option': 'LOAN',
        }
        data['values'].append(loan_result)
    
    print data
    ddata = {
    'budget': 300,
    'values': [
        {
            'True monthly cost': 408, 
            'Regular monthly payment': 716,
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
  
    return JsonResponse(data)