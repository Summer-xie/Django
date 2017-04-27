# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Redbag(models.Model):
        number = models.CharField(max_length=10)
        total = models.CharField(max_length=10)
        xuhao = models.CharField(max_length=10)
        single = models.CharField(max_length=10)
        datetime= models.DateTimeField(auto_now_add = True)

