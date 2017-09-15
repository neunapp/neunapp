# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#import python library
import re
import sys

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
from django.views.generic.edit import FormView

#import forms.py
from .forms import CitationForm

#import models.py
from .models import Citation, Product


class ProductosView(ListView):
    """ Lista todos los productos """

    context_object_name = 'product'
    template_name = 'productos/index.html'

    def get_queryset(self):
        #
        queryset = Product.objects.filter(
            published=True,
        )
        return queryset


class ProductDetailview(DetailView):
    """
    vista que muetra el detalle de un producto
    """

    model = Product
    template_name = 'productos/producto/detail.html'


# Create your views here.
class CitationCreateView(CreateView):
    ''' registrar una nueva cita '''

    form_class = CitationForm
    success_url = reverse_lazy('home_app:mensaje')
    template_name = 'productos/cita/index.html'


class CitationProductCreateView(FormView):
    """
       vista para registrar una cita de un producto
    """

    form_class = CitationForm
    success_url = reverse_lazy('producto_app:product_citation-add')
    template_name = 'producto/citationbyproductadd.html'

    def form_valid(self, form):
        pk = self.kwargs['pk']
        product = Product.objects.get(pk=pk)
        cita = form.save(commit=False)
        #
        cita.product = product
        cita.save()
        return super(CitationProductCreateView, self).form_valid(form)


# class CitationProductCreateView(FormView):
#     """
#        create view para
#     """
#     form_class = CitationForm
#     success_url = reverse_lazy('producto_app:product_citation-add')
#     template_name = 'producto/citationbyproductadd.html'
#
#     def form_valid(self, form):
#         pk = self.kwargs['pk']
#         product = Product.objects.get(pk=pk)
#         print product
#         email = form.cleaned_data['email']
#         phone = form.cleaned_data['phone']
#         address = form.cleaned_data['address']
#         name = form.cleaned_data['name']
#         hour_atention = form.cleaned_data['hour_atention']
#         day_atention = form.cleaned_data['day_atention']
#
#         citation = Citation(
#             email = email,
#             phone = phone,
#             address = address,
#             name = name,
#             hour_atention = hour_atention,
#             day_atention = day_atention,
#             product=product
#         )
#         citation.save()
#
#         return super(CitationbyProductCreateView, self).form_valid(form)
