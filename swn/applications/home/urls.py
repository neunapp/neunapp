# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url para pantalla principal
    url(r'^$',
        views.HomeView.as_view(),
        name='index'
    ),
    #url para mensaje
    url(r'^solicitud-confirmada/$',
        views.MensajeView.as_view(),
        name='mensaje'
    ),
]
