# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)

    class Meta:
        ordering = ('created',)



class ColdStorage(models.Model):
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    yieldType = models.CharField(max_length=50,null=True)
    space = models.FloatField(null=True, blank=True)
    empty = models.FloatField(null=True, blank=True,default=0.0)

    class Meta:
        ordering = ('created',)