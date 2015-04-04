"""
Views/Controllers
"""
import datetime
from rest_framework import mixins, viewsets
 
from .models import Job, CarMake, CarModel
from .serializers import JobSerializer, CarModelSerializer

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('main.html')


def about(request):
    return render_to_response('about.html')


def test_json(request):
    data = {
    'budget': 300,
    'values': [
        {
            'Real World Out of Pocket': 408, 
            'Effective Monthly': 716,
            'financial_option': 'HP',
        },
        {
            'Real World Out of Pocket': 500, 
            'Effective Monthly': 463,
            'financial_option': 'PCP',
        },
        {
            'Real World Out of Pocket': 408, 
            'Effective Monthly': 313,
            'financial_option': 'LEASE',
        },
        {
            'Real World Out of Pocket': 336, 
            'Effective Monthly': 674,
            'financial_option': 'LOAN',
        },
    ]}
  
    return JsonResponse(data)