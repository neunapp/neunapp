# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product, Citation, ProductPropertys, ProductSolicitude
# Register your models here.

admin.site.register(Product)
admin.site.register(Citation)
admin.site.register(ProductPropertys)
admin.site.register(ProductSolicitude)
