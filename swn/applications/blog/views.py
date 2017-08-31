# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import (
    CreateView,
    UpdateView,
    TemplateView,
    DeleteView,
    DetailView,
    FormView,
    ListView
)
# Create your views here.

#app blog
from .models import Blog, Category
from .forms import SearchForm


class BlogListView(ListView):
   context_object_name = 'blogs'
   template_name = 'blog/list.html'

   def get_context_data(self, **kwargs):
       context = super(BlogListView, self).get_context_data(**kwargs)
       context['form'] = SearchForm
       context['categorias'] = Category.objects.list_category()
       return context

   def get_queryset(self):
       #recuperamos el valor por GET
       q = self.request.GET.get("kword", '')
       queryset = Blog.objects.search_blog(q)
       #queryset_category = Category.objects.list_category()
       return queryset
      # return {'blogs':queryset,'categories':queryset_category}


class BlogCategoriaListView(ListView):
   """vista que lista caterias por blog"""

   context_object_name = 'categories'
   template_name = 'blog/by_category.html'

   def get_context_data(self, **kwargs):
       context = super(BlogCategoriaListView, self).get_context_data(**kwargs)
       category = self.kwargs['slug']
       context['form'] = SearchForm
       context['blogs'] = Blog.objects.search_blog_by_category(category)
       return context

   def get_queryset(self):
       #recuperamos el valor por GET
       blog = self.request.GET.get("kword", '')
       category = self.kwargs['slug']
       queryset = Blog.objects.search_blogxcategory(category)
       #queryset_category = Category.objects.list_category()
       return queryset
      # return {'blogs':queryset,'categories':queryset_category}