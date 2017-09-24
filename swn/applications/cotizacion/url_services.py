# django
from django.conf.urls import include, url

# local
from . import viewsets


urlpatterns = [
    url(r'^api/cotizacion/tipo/$',
        viewsets.TypeQuoteListViewSet.as_view({'get': 'list'}),
        name='api_cotizacion-list_tipo'
    ),
    url(r'^api/cotizacion/questions/(?P<pk>[-\w]+)/$',
        viewsets.QuestionListViewSet.as_view({'get': 'list'}),
        name='api_cotizacion-list_questions'
    ),
    url(r'^api/cotizacion/questions/answer/(?P<pk>[-\w]+)/$',
        viewsets.AnswerListViewSet.as_view({'get': 'list'}),
        name='api_cotizacion-list_answers'
    ),
    url(r'^api/cotizacion/solicitud/save/$',
        viewsets.RequestQuoteViewSet.as_view({'post': 'create'}),
        name='api_cotizacion-request_quote'
    ),
]
