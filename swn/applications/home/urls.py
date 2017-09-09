from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url para home
    url(r'^citacion/$',
        views.CitationCreateView.as_view(),
        name='home_citation-add'
    ),

]