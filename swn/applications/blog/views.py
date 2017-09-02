# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

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

#app blog
from .models import Blog, Category, Commentary
#local forms
from .forms import SearchForm,ComentarybyBlogForm



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



class BLogDetailview(DetailView):
    """
    vista que muestra detalle blog 
    """

    context_object_name = 'blogs'
    model = Blog
    template_name = 'blog/detail.html'



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
        context['blog'] = Blog.objects.filter(pk=blog.pk)
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



