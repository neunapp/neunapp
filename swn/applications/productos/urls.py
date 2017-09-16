from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url para index de productos o vitrina
    url(r'^nuestros-productos-de-software-cusco/$',
        views.ProductosView.as_view(),
        name='productos-index'
    ),
    #url para ver el detalede un producto
    url(r'^software-cusco/(?P<slug>[-\w]+)/$',
        views.ProductDetailview.as_view(),
        name='productos-detail'
    ),
    #url para index de cita
    url(r'^registrar-cita/$',
        views.CitationCreateView.as_view(),
        name='productos_cita-index'
    ),
    #url para registrar cita de producto
    url(r'^reservar-cita/(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
        views.CitationProductCreateView.as_view(),
        name='productos_cita-add'
    ),
]
