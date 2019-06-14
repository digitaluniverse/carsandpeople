# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

import datetime

# Create your models here.
YEAR_CHOICES = [(r,r) for r in range(1885, datetime.date.today().year+1)]

class Person(models.Model):
    name = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=35)
    drivers_license = models.CharField(max_length=8)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Car(models.Model):
    car_model = models.CharField(max_length=20)
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    license_plate = models.CharField(max_length=8, unique=True)
    picture = models.ImageField(upload_to='media/cars/pictures/%Y/%m/%d',
                              blank=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='cars')
    def __str__(self):
        return self.car_model
