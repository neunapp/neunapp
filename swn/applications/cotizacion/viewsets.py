#libreries rest_framework
from rest_framework import viewsets
from rest_framework.response import Response
#django import
from django.shortcuts import get_object_or_404

#local impotrs
from .serializers import (
    QuestionSerializer,
    AnswerSerializer,
    RequestQuoteSerializer
)

from .models import Question, Answer, RequestQuote


class QuestionListViewSet(viewsets.ModelViewSet):
    '''
    servicio para listar preguntas
    '''
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.order_by('order')
        return queryset


class AnswerListViewSet(viewsets.ModelViewSet):
    '''
    servicio para listar respuestas de preguntas
    '''
    serializer_class = AnswerSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = Answer.objects.filter(
            question__pk=pk,
        ).order_by('order')
        return queryset


class RequestQuoteViewSet(viewsets.ViewSet):
    ''''
    servicio para registrar solicitud de cotizacion
    '''

    def create(self, request):
        serializado = RequestQuoteSerializer(data=request.data)
        if serializado.is_valid():
            serializado.save()
            print 'solicitud de cotizacion gurdada'
        else:
            print serializado.errors

        return Response()
