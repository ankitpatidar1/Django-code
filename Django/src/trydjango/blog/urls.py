from django.conf.urls import url
from django.urls import path

from django.contrib import admin
from .views import *
app_name = 'blog'
urlpatterns = [
    path("", ArticleListView.as_view(), name="blog-list"),
    path("create/", ArticleCreateView.as_view(), name="blog-create"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="blog-detail"),
    path("<int:pk>/update/", ArticleUpdateView.as_view(), name="blog-update"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="blog-delete")
]