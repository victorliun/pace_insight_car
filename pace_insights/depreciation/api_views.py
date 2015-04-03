"""
Views/Controllers
"""
from rest_framework import mixins, viewsets
 
from .models import Job, CarMake, CarModel, CarVersion, Depreciation
from .api_filters import (
    CarModelFilter, CarMakeFilter, CarVersionFilter,
    DepreciationFilter)
from .serializers import (
    JobSerializer, CarMakeSerializer, CarModelSerializer,
    CarVersionSerializer, DepreciationSerializer)


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


class CarModelViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """
    API endpoint that allows car model to be viewed or created.
    """
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    filter_class = CarModelFilter


class CarMakeViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """
    API endpoint that allows car model to be viewed or created.
    """
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer
    filter_class = CarMakeFilter


class CarVersionViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """
    API endpoint that allows car model to be viewed or created.
    """
    queryset = CarVersion.objects.all()
    serializer_class = CarVersionSerializer
    filter_class = CarVersionFilter

class DepreciationViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """
    API endpoint that allows car model to be viewed or created.
    """
    queryset = Depreciation.objects.all()
    serializer_class = DepreciationSerializer
    filter_class = DepreciationFilter