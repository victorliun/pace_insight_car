from rest_framework import serializers
 
from .models import Job, CarModel, CarMake, CarVersion, Depreciation
 
 
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job

 
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake


class CarVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarVersion


class DepreciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Depreciation
