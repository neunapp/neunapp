from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url para pagina principal de blog
    url(r'^articulos-en-empresas-y-desarrollo-de-sistemas-web-cusco/blog$',
        views.BlogView.as_view(),
        name='blog-index'
    ),
    #url para filtrar por categoria principal
    url(r'^sistemas-web-cusco/(?P<slug>[-\w]+)/$',
        views.FilterBlogView.as_view(),
        name='blog-filter'
    ),
    #url para ver el detalede un blog
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
