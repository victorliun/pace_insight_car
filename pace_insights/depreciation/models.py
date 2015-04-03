# -*- coding: utf-8 -*-
'''
Models for depreciation.
'''
import logging

from datetime import datetime, timedelta

from django.db import models

logger = logging.getLogger(__file__)


class CarRoadTax(models.Model):
    """
    Model of car road tax.
    """
    band = models.CharField(max_length=8, unique=True)
    co2 = models.CharField(max_length=64)
    first_year_rate = models.CharField(max_length=64)
    standard_rate = models.CharField(max_length=64)


class CarMake(models.Model):
    """
    Model of car_make table.
    """
    name = models.CharField(max_length=64, unique=True)
    whatcar_id = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True, auto_now=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{}'.format(self.name)

    class Meta:
        verbose_name_plural = 'Car Makes'


class CarModel(models.Model):
    """
    Model of car_model table.
    """
    name = models.CharField(max_length=64)
    whatcar_id = models.IntegerField(default=0)
    car_make = models.ForeignKey(CarMake, related_name="car_models")
    create_time = models.DateTimeField(auto_now_add=True, auto_now=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{} - {}'.format(
            self.car_make.name,
            self.name
        )

    @property
    def full_name(self):
        '''Return car make and model name.'''

        return u'{} {}'.format(self.car_make.name, self.name)

    class Meta:
        verbose_name_plural = 'Car Models'
        unique_together = ("name", "car_make")


class CarVersion(models.Model):
    """
    Model of car_version table.
    """
    name = models.CharField(max_length=64)
    whatcar_id = models.IntegerField(default=0)
    doors = models.IntegerField(default=0)
    body_range = models.CharField(max_length=64, null=True)
    car_model = models.ForeignKey(CarModel, related_name="car_versions")
    create_time = models.DateTimeField(auto_now_add=True, auto_now=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.full_name

    @property
    def full_name(self):
        '''Return car make and model name.'''

        return u'{} {} {}'.format(
            self.car_model.car_make.name,
            self.car_model.name,
            self.name
        )

    @property
    def latest_depreciation(self):
        '''Return latest depreciation.'''

        return self.depreciations.latest()
    
    class Meta:
        verbose_name_plural = 'Car Versions'
        unique_together = ("name", "car_model")


class Depreciation(models.Model):
    '''Model for depreciation table, which stores the depreciation of
    a car in 4 years time.
    '''

    car_version = models.ForeignKey(CarVersion, related_name="depreciations")
    create_time = models.DateTimeField(auto_now_add=True, auto_now=True)
    year_0 = models.CharField(max_length=16)
    year_1 = models.CharField(max_length=16)
    year_2 = models.CharField(max_length=16)
    year_3 = models.CharField(max_length=16)
    year_4 = models.CharField(max_length=16)
    year_0_mock = models.CharField(max_length=16, blank=True)
    year_1_mock = models.CharField(max_length=16, blank=True)
    year_2_mock = models.CharField(max_length=16, blank=True)
    year_3_mock = models.CharField(max_length=16, blank=True)
    year_4_mock = models.CharField(max_length=16, blank=True)

    def __unicode__(self):
        return u"{}:[{}, {}, {}, {}, {}]".format(
            self.car_version.full_name,
            (self.year_0, self.year_0_mock),
            (self.year_1, self.year_1_mock),
            (self.year_2, self.year_2_mock),
            (self.year_3, self.year_3_mock),
            (self.year_4, self.year_4_mock),
        )

    def get_raw_data(self):
        '''Return original depreciation data'''
        return [self.year_0, self.year_1,
            self.year_2, self.year_3, self.year_4]

    def get_addon_data(self):
        '''Return original depreciation data'''
        return [self.year_0_mock, self.year_1_mock,
            self.year_2_mock, self.year_3_mock, self.year_4_mock]

    class Meta:
        verbose_name_plural = 'Depreciations'
        get_latest_by = "create_time"
        ordering = ['-create_time',]


class FinancialOption(models.Model):
    '''Model for financial options.'''

    name = models.CharField(max_length=16)
    create_time = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __unicode__(self):
        return self.name


class Job(models.Model):
    """Class describing a computational job"""
 
    # currently, available types of job are:
    TYPES = (
        ('scrapping', 'scrapping'),
    )
 
    # list of statuses that job can have
    STATUSES = (
        ('start', 'start'),
        ('running', 'running'),
        ('finished', 'finished'),
        ('failed', 'failed'),
    )
 
    job_type = models.CharField(choices=TYPES, max_length=20)
    status = models.CharField(choices=STATUSES, max_length=20)
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    def __unicode__(self):
        return u'{}:{}'.format(self.job_type, self.status)

    def save(self, *args, **kwargs):
        """Save model and if job is in pending state, schedule it"""
        super(Job, self).save(*args, **kwargs)
        if self.status == 'start':
            from .tasks import TASK_MAPPING
            task = TASK_MAPPING[self.job_type]
            task.delay(job_id=self.id)
