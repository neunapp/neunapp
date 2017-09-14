from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url para pantalla principal
    url(r'^$',
        views.HomeView.as_view(),
        name='index'
    ),
    #
    url(r'^citacion/$',
        views.CitationCreateView.as_view(),
        name='home_citation-add'
    ),

]
