# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import TypeQuote, RequestQuote, Question, Answer
# Register your models here.
''
class CotizacionAdmin(admin.ModelAdmin):
   list_display = (
       'email',
       'phone',
       'message',
       'amount'
   )
   search_fields = ('email', 'phone')
   list_filter = ('typequote',)


admin.site.register(RequestQuote, CotizacionAdmin )


admin.site.register(TypeQuote)
admin.site.register(Question)
admin.site.register(Answer)
