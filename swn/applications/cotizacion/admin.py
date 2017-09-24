# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import RequestQuote, Question, Answer, TypeQuote
#

class TypeQuoteAdmin(admin.ModelAdmin):
    list_display = (
        'answer',
        'amount',
        'order',
        'description'
    )
    search_fields = ('answer',)


class CotizacionAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'phone',
        'message',
        'amount'
    )
    search_fields = ('email', 'phone')


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'description',
        'order'
    )
    search_fields = ('description', 'question')


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'description',
        'amount',
        'estilo',
        'order'
    )
    search_fields = ('answer', 'question')

admin.site.register(TypeQuote, TypeQuoteAdmin )
admin.site.register(RequestQuote, CotizacionAdmin )
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
