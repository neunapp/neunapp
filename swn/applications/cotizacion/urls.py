from django.conf.urls import include, url
from . import views

urlpatterns = [
    #para index de cotizacion
    url(r'^cotiza-tu-proyecto-de-software-cusco/$',
        views.CotizacionView.as_view(),
        name='cotizacion-index'
    ),

]
