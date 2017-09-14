from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url para index de productos o vitrina
    url(r'^nuestros-productos-de-software-cusco/$',
        views.ProductosView.as_view(),
        name='productos-index'
    ),
    #url para index de cita
    url(r'^registrar-cita/$',
        views.CitationView.as_view(),
        name='productos_cita-index'
    ),
]
