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
from django.conf.urls import url , include
from django.contrib import admin
from product.views import *
from polls import views

urlpatterns = [
    path("", home_view, name='home'),
    path("home/", home_view, name='home'),
    path("contact/", contact_view, name='contact'),
    path("social/", social_view, name='social'),
    path("about/", about_view, name='about'),
    path('admin/', admin.site.urls),
    path('product/',  include('product.urls')),
    path('blog/',  include('blog.urls'))
]

# app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.IndexView.as_view(), name='index'),
#     # ex: /polls/5/
#     path('polls/<int:pk>/', views.DetailView.as_view(), name='detail'),
#     # ex: /polls/5/results/
#     path('polls/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     # ex: /polls/5/vote/
#     path('polls/<int:question_id>/vote/', views.vote, name='vote'),
#     url(r'^admin/', admin.site.urls)
# ]
