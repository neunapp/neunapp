# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Blog, Category, Subscription, Tag, Commentary
# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Subscription)
admin.site.register(Tag)
admin.site.register(Commentary)