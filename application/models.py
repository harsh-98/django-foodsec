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