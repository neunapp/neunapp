# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#django library
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    FormView,
    UpdateView,
    DetailView,
    DeleteView,
    ListView,
    TemplateView,
    View,
)

#import forms.py
from .forms import CitationForm

#import models.py

from .models import Citation, Product




# Create your views here.
class CitationCreateView(CreateView):
    '''registrar un proveedor'''
    form_class = CitationForm
    success_url = reverse_lazy('producto_app:home_citation-add')
    template_name = 'producto/addcitation.html'

    def form_valid(self, form):
        citation = form.save(commit=False)
        #email = form.cleaned_data['email']
        #phone = form.cleaned_data['phone']
        #regex = re.match("(\w+)@(\wnet|com]", sys.argv[1])
        citation.save()

        return super(CitationCreateView, self).form_valid(form)


class CitationbyProductCreateView(FormView):
    """
       create view para 
    """
    form_class = CitationForm
    success_url = reverse_lazy('producto_app:product_citation-add')
    template_name = 'producto/citationbyproductadd.html'

    def form_valid(self, form):
        pk = self.kwargs['pk']
        product = Product.objects.get(pk=pk)
        print product
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        address = form.cleaned_data['address']
        name = form.cleaned_data['name']
        hour_atention = form.cleaned_data['hour_atention']
        day_atention = form.cleaned_data['day_atention']

        citation = Citation(
            email = email,
            phone = phone,
            address = address,
            name = name,
            hour_atention = hour_atention,
            day_atention = day_atention,
            product=product
        )
        citation.save()

        return super(CitationbyProductCreateView, self).form_valid(form)



