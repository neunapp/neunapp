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
from .models import Blog
from .forms import SearchForm


class BlogListView(ListView):
   context_object_name = 'blogs'
   template_name = 'blog/list.html'

   def get_context_data(self, **kwargs):
       context = super(BlogListView, self).get_context_data(**kwargs)
       context['form'] = SearchForm
       return context

   def get_queryset(self):
       #recuperamos el valor por GET
       q = self.request.GET.get("kword", '')
       queryset = Blog.objects.search_blog(q)
       return queryset