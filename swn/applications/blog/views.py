# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse

from django.views.generic import (
    CreateView,
    UpdateView,
    TemplateView,
    DeleteView,
    DetailView,
    FormView,
    ListView
)

from django.views.generic.edit import FormMixin
# Create your views here.

#application home
from applications.home.forms import BlogSuscriptionForm

#app blog
from .models import Blog, Category, Commentary, MasterCategory
#local forms
from .forms import SearchForm,ComentarybyBlogForm


#vistas para blog
class BlogView(ListView):
    """ pantalla principal de blog"""

    context_object_name = 'blogs'
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        context['master_categorys'] = MasterCategory.objects.order_by('created')
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        q = self.request.GET.get("kword", '')
        queryset = Blog.objects.search_blog(q)
        return queryset


#vistas para blog
class FilterBlogView(ListView):
    """ pantalla principal con filtro de blog"""

    context_object_name = 'blogs'
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(FilterBlogView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        context['master_categorys'] = MasterCategory.objects.order_by('created')
        return context

    def get_queryset(self):
        #recuperamos valor de url
        master_category = self.kwargs['slug']
        #recuperamos el valor por GET
        q = self.request.GET.get("kword", '')
        queryset = Blog.objects.filter_blog_by_master_category(master_category,q)
        return queryset


class BLogDetailview(FormMixin, DetailView):
    """
    vista que muestra detalle blog
    """

    model = Blog
    #formlario para suscripcion
    form_class = BlogSuscriptionForm
    template_name = 'blog/detail.html'

    def get_success_url(self):
        return '.'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(BLogDetailview, self).form_valid(form)


###
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
   """
   vista que lista caterias por blog
   """

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


class BlogCreatedComentaryView(FormMixin, DetailView):
    """
    vista que su agrega un comentario blog
    """

    model = Blog
    template_name = 'blog/detail.html'
    form_class = ComentarybyBlogForm

    def get_success_url(self):
        return reverse_lazy('/')


    def get_context_data(self, **kwargs):
        context = super(BlogCreatedComentaryView, self).get_context_data(**kwargs)
        context['form']= self.get_form()
        #obtenemos'

        blog = self.object
        context['commentary'] = Commentary.objects.filter(blog=blog).order_by('-created')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):

        email = form.cleaned_data['email']

        nick = form.cleaned_data['nick']

        description = form.cleaned_data['description']

        blog = self.object

        comentario = Commentary(
            email = email,
            nick = nick,
            description = description,
            blog = blog
        )
        comentario.save()
        return super(BlogCreatedComentaryView, self).form_valid(form)
