from rest_framework import serializers
 
from .models import Job, CarModel, CarMake, CarVersion, Depreciation
 
 
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job

 
class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        exclude = ('whatcar_id', 'create_time', 'update_time')


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        exclude = ('whatcar_id', 'create_time', 'update_time')


class CarVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarVersion
        exclude = ('whatcar_id', 'create_time', 'update_time')


class DepreciationSerializer(serializers.ModelSerializer):
    car_full_name = serializers.SerializerMethodField()

    def get_car_full_name(self, obj):
        return obj.car_version.full_name

    class Meta:
        model = Depreciation
        fields = ('id', 'car_version', 'year_0', 'year_1',
            'year_2', 'year_3', 'year_4', 'car_full_name')
            # 'year_2_mock', 'year_3_mock', 'year_4_mock', 'car_full_name')
