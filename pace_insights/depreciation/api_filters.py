"""
Module for api filters
"""
import django_filters

from .models import Job, CarMake, CarModel, Depreciation, CarVersion


class CarMakeFilter(django_filters.FilterSet):
    class Meta:
        model = CarMake
        fields = ['name', ]


class CarModelFilter(django_filters.FilterSet):
    class Meta:
        model = CarModel
        fields = ['car_make', ]


class CarVersionFilter(django_filters.FilterSet):
    class Meta:
        model = CarVersion
        fields = ['car_model', ]


class DepreciationFilter(django_filters.FilterSet):
    class Meta:
        model = Depreciation
        fields = ['car_version', ]
