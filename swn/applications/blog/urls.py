from django.conf.urls import include, url
from . import views

urlpatterns = [
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
        name='blog-detail'
    ),

]