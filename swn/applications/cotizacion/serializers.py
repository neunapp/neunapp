from rest_framework import serializers

from .models import Answer, Question, RequestQuote, TypeQuote


class TypeQuoteSerializer(serializers.ModelSerializer):
    """serializador para listar tipo de cotizcion"""

    class Meta:
        model = TypeQuote
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    """serializador para listar pregunta de un titpo cotizacion"""

    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    """serializador para listar respuestas de una pregunta"""

    class Meta:
        model = Answer
        fields = '__all__'


class RequestQuoteSerializer(serializers.ModelSerializer):
    """serializador para registrar solicitud de cotizacion"""

    class Meta:
        model = RequestQuote
        fields = (
            'email',
            'phone',
            'message',
            'amount',
            'answer',
            'question',
        )
