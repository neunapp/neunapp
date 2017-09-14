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


class CotizacionView(TemplateView):
    """ pantalla principal de cotizacion"""
    template_name = 'cotizacion/index.html'
