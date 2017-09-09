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

#import forms.py
from .forms import CitationForm

# Create your views here.
class CitationCreateView(CreateView):
    '''registrar un proveedor'''
    form_class = CitationForm
    success_url = reverse_lazy('home_app:home_citation-add')
    template_name = 'home/addcitation.html'

    def form_valid(self, form):
        citation = form.save(commit=False)
        #email = form.cleaned_data['email']
        #phone = form.cleaned_data['phone']
        #regex = re.match("(\w+)@(\wnet|com]", sys.argv[1])
        citation.save()

        return super(CitationCreateView, self).form_valid(form)