from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url para home
    url(r'^citacion/(?P<pk>\w+)/$',
        views.CitationbyProductCreateView.as_view(),
        name='product_citation-add'
    ),


]