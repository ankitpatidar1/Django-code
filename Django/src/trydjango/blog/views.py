# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render
from .models import Article
from .forms import ArticleModelForm
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ( CreateView, 
                                   ListView, 
                                   UpdateView, 
                                   DeleteView,
                                   ListView,
                                   DetailView)

# Create your views here.
class ArticleCreateView(CreateView):
    template_name = 'article/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self,form):
        print (form.cleaned_data)
        return super().form_valid(form)

class ArticleListView(ListView):
    template_name = 'article/article_list.html'
    queryset = Article.objects.all()
    

class ArticleDetailView(DetailView):
    template_name = 'article/article_detail.html'
    queryset = Article.objects.all()
    def get_object(self):
        id_ =  self.kwargs.get("pk")
        return get_object_or_404(Article,id=id_)
    

class ArticleUpdateView(UpdateView):
    template_name = 'article/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    def get_object(self):
        id_ =  self.kwargs.get("pk")
        return get_object_or_404(Article,id=id_)
    def form_valid(self,form):
        print (form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'article/article_delete.html'
    # form_class = ArticleModelForm
    # queryset = Article.objects.all()
    def get_object(self):
        id_ =  self.kwargs.get("pk")
        return get_object_or_404(Article,id=id_)

    def get_success_url(self):
        return reverse("blog:blog-list")



