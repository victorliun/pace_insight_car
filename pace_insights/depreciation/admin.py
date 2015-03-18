"""
Models Admin for depreciation.
"""

from django.contrib import admin

from depreciation.models import (
    Job,
    CarMake,
    CarModel,
    CarVersion,
    Depreciation,
    FinancialOption,
    CarRoadTax,
)


class CarMakeAdmin(admin.ModelAdmin):
    """CarMake admin"""
    list_display = ['id', 'get_name', 'whatcar_id', 'create_time',
        'update_time']

    def get_name(self, obj):
        return obj.name
    get_name.short_description = 'Make'


class CarModelAdmin(admin.ModelAdmin):
    """CarMake admin"""
    list_display = ['id', 'get_car_make', 'get_name', 'whatcar_id',
        'create_time', 'update_time']
    
    def get_car_make(self, obj):
        return obj.car_make.name
    get_car_make.short_description = 'Make'

    def get_name(self, obj):
        return obj.name
    get_name.short_description = 'Model'



class CarVersionAdmin(admin.ModelAdmin):
    """CarMake admin"""
    list_display = ['id', 'get_car_make', 'get_car_model', 'get_name',
        'body_range', 'doors', 'whatcar_id', 'create_time',]
    
    def get_name(self, obj):
        return obj.name
    get_name.short_description = 'Version'

    def get_car_make(self, obj):
        return obj.car_model.car_make.name
    get_car_make.short_description = 'Make'

    def get_car_model(self, obj):
        return obj.car_model.name
    get_car_make.short_description = 'Model'

    list_filter = ('car_model__car_make',)


class DepreciationAdmin(admin.ModelAdmin):
    """CarMake admin"""
    list_display = ['id', 'car_version', 'year_0', 'year_0_mock', 'year_1',
        'year_1_mock', 'year_2', 'year_2_mock', 'year_3', 'year_3_mock',
        'year_4', 'year_4_mock', 'create_time']
    list_filter = ('car_version__car_model__car_make',)


class FinancialOptionAdmin(admin.ModelAdmin):
    """CarMake admin"""
    list_display = ['id', 'name','create_time']


class JobAdmin(admin.ModelAdmin):
    """JOb admin"""
    list_display = ['job_type', 'status','created_at', 'updated_at']


class CarRoadTaxAdmin(admin.ModelAdmin):
    """JOb admin"""
    list_display = ['id', 'band', 'co2','first_year_rate',
        'standard_rate']

# Register your models here.
admin.site.register(Job, JobAdmin)
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarRoadTax, CarRoadTaxAdmin)
admin.site.register(CarVersion, CarVersionAdmin)
admin.site.register(Depreciation, DepreciationAdmin)
admin.site.register(FinancialOption, FinancialOptionAdmin)