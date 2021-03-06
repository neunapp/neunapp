# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Blog, Category, Subscription, Tag, Commentary, MasterCategory
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
   list_display = (
       'title',
       'description',
       'published',
       'created_by',
       'category',
       'created'
   )
   search_fields = ('title', 'description')
   list_filter = ('category',)
   #campos para agregar
   fields =(
        'title',
        'description',
        'content',
        'category',
        'image',
        'tag',
        'published',
        'author',
        'created_by',
        'modified_by',
   )
   #solo si hay many to many
   filter_horizontal = ('tag',)


admin.site.register(Blog, BlogAdmin )

admin.site.register(Category)
admin.site.register(Subscription)
admin.site.register(Tag)
admin.site.register(Commentary)
admin.site.register(MasterCategory)
