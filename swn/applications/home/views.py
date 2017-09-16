# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#django library
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    TemplateView,
    View,
)

#import app blog
from applications.blog.models import Blog
#import app productos
from applications.productos.models import Product

#import forms.py
from .forms import SuscriptionForm


class MensajeView(TemplateView):
    template_name = 'home/mensaje.html'


class HomeView(CreateView):
    '''registrar nuevo registro de suscripcion'''

    form_class = SuscriptionForm
    success_url = reverse_lazy('home_app:index')
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['blogs'] = Blog.objects.search_blog('')[:3]
        #recupeamos productos principales
        prods = Product.objects.principal_product()
        #enviamos prods al home
        context['producto_1'] = prods[3]
        context['producto_2'] = prods[2]
        context['producto_3'] = prods[1]
        context['producto_4'] = prods[0]
        return context
