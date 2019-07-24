# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from rest_framework import generics , mixins
from django.shortcuts import render, get_object_or_404,redirect
from product.models import Product
from .serializers import ProductSerializer
from .forms import ProductForm , RawProductForm

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
def product_list_view(request):
    obj = Product.objects.all()
    context = {"product_list":obj}
    return render(request,'product/product_list.html',context)
def product_delete_view(request,id):
    obj = get_object_or_404(Product,id=id)
    #post request
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context = {"object":obj}
    return render(request,'product/product_delete.html',context)
def render_initial_data(request):
    initial_data = {
        "title":"my this awesome title"
    }
    _object = Product.objects.get(id=10)
    form = ProductForm(request.POST or None , initial=initial_data,instance=_object)
    context = {"form":form}
    return render(request,'product/product_create.html',context)

def dynamic_lookup_view(request,id):
    #obj = get_object_or_404(Product,id=id)
    # obj = Product.objects.get(id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {"obj":obj}
    return render(request,'product/detail.html',context)

def product_create_view(request):
    form = RawProductForm()
    if request.method == 'GET':
        form = RawProductForm(request.GET or None)
    elif request.method == 'POST':
        form = RawProductForm(request.POST or None)
    context = { "form":form }
    if form.is_valid():
        print (form.cleaned_data)
        Product.objects.create(**form.cleaned_data)
    else:
        print (form.errors)
    return render(request,'product/product_create.html',context)


# def product_create_view(request):
#     form = ProductForm(request.GET or None)
#     print ("request",request)
#     if form.is_valid():
#         form.save()
#     context = { "form":form }
#     return render(request,'product/product_create.html',context)
def product_detail_view(request ,id):
    obj = Product.objects.get(id=id)
    context = {"obj":obj}
    return render(request,'product/detail.html',context)
def home_view(request,*arge, **kargs):
    return render(request,"home.html",{})
def contact_view(*arge, **kargs):
    return render(request,"contact.html",{})
def about_view(request,*arge, **kargs):
    my_dict = {"text" : 'ankit',
        "contact_number" : 'asdfg',
        "arr" : [1234,234,2345]
    }
    return render(request,"about.html",my_dict)
def social_view(*arge, **kargs):
    return render(request,"social.html",{})