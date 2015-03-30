"""
Views/Controllers
"""
import datetime
from rest_framework import mixins, viewsets
 
from .models import Job
from .serializers import JobSerializer

from django.http import HttpResponse
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