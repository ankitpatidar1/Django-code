"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path

from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from polls import views

urlpatterns = [
    path("", product_list_view, name="product-list"),
    path("create/", render_initial_data, name="product-create"),
    path("<int:id>/", product_detail_view, name="product-update"),
    path("<int:id>/delete/", product_delete_view, name="product-delete"),
    path('api/',  include('apis.urls'))
]