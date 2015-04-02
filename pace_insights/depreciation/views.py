"""
Views/Controllers
"""
import datetime
from rest_framework import mixins, viewsets
 
from .models import Job
from .serializers import JobSerializer

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('index.html')

class JobViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """
    API endpoint that allows jobs to be viewed or created.
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer


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