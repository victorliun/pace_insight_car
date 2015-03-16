from rest_framework import mixins, viewsets
 
from .models import Job
from .serializers import JobSerializer

from django.http import HttpResponse
import datetime

def home(request):
    html = """
    <html>
        <body>
            <h1>Welcome to car finance compared. </h1>
            <a href='/admin/'>Go to admin page.</a>
        </body>
    </html>"""
    return HttpResponse(html)

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