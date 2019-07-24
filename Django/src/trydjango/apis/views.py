# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from rest_framework import generics , mixins
from django.shortcuts import render, get_object_or_404,redirect
from product.models import Product
from .serializers import ProductSerializer
from product.forms import ProductForm , RawProductForm

class ProductRudView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Product.objects.get(pk=pk)

class ProductListView(mixins.CreateModelMixin,generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(description__icontains=query)).distinct()
        return qs
        return Product.objects.all()
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    
    # def get_queryset(self):
    #     return Product.objects.all()

# Create your views here.