from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url para pagina principal de blog
    url(r'^articulos-relacionados-empresas-tecnologia/$',
        views.BlogView.as_view(),
        name='blog-index'
    ),
    url(r'^blog-leer/(?P<slug>[-\w]+)/$',
        views.BLogDetailview.as_view(),
        name='blog-detail'
    ),

    #url para home
    url(r'^blog/(?P<slug>\w+)/$',
        views.BlogCategoriaListView.as_view(),
        name='blog_category-list'
    ),

    url(r'^blog$',
        views.BlogListView.as_view(),
        name='blog-list'
    ),

    url(
        r'^blog/(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$',
        views.BlogCreatedComentaryView.as_view(),
        name='blog-detail_come'
    ),

]
