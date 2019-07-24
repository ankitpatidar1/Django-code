# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models

# Create your models here.
class  Product(models.Model):
    title  = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10000) 
    summary = models.TextField(default='test text')
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("product-update" ,kwargs={"id":self.id})
        
    def __str__(self):
        return self.title