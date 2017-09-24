# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel


#django library
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.postgres.fields import ArrayField


@python_2_unicode_compatible
class TypeQuote(TimeStampedModel):
    """ modelo para respuestas """

    answer = models.CharField(blank=True, max_length=200)
    image = models.ImageField('imagen', upload_to='answer')
    description = models.CharField('Descripcion',blank=True, max_length=300)
    amount = models.DecimalField('Monto',max_digits=10, decimal_places=2, default=0)
    estilo = models.CharField(blank=True, max_length=100)
    order = models.IntegerField('orden', default=0)

    class Meta:
        verbose_name = 'Tipo de Cotizacion'
        verbose_name_plural = 'Tipos de Cotizaciones'
        ordering = ['order']


    def __str__(self):
        return str(self.answer)


@python_2_unicode_compatible
class RequestQuote(TimeStampedModel):
    """
        datamodel RequestQuote
    """

    email = models.EmailField('email')
    phone = models.CharField('telefono', max_length=12, blank=True)
    message= models.CharField('mensaje', max_length=300, blank=True)
    amount = models.IntegerField('monto', default=0)
    answer = ArrayField(
        models.CharField('Respuesta',max_length=7, blank=True),
        blank=True,
        null=True
    )
    question = ArrayField(
        models.CharField('pregunta',max_length=7, blank=True),
        blank=True,
        null=True
    )


    class Meta:
        verbose_name = 'Solicitud de Cotizacion'
        verbose_name_plural = 'Solicitudes de cotizacion'
        ordering = ['-created']

    def __str__(self):
        return self.email



@python_2_unicode_compatible
class Question(TimeStampedModel):
    """ modelo para pregunta """

    typequote = models.ForeignKey(
        TypeQuote,
        blank=True,
        null=True,
        verbose_name='question_tipo_cotiacion',
    )
    question = models.CharField('pregunta', max_length=300)
    description = models.CharField('descripcion', max_length=200)
    order = models.IntegerField('orden')

    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'
        ordering = ['-created']

    def __str__(self):
        return self.question



@python_2_unicode_compatible
class Answer(TimeStampedModel):
    """ modelo para respuestas """

    question = models.ForeignKey(Question, verbose_name='pregunta_cotiacion')
    answer = models.CharField(blank=True, max_length=200)
    image = models.ImageField('imagen', upload_to='answer')
    description = models.CharField('Descripcion',blank=True, max_length=300)
    amount = models.DecimalField('Monto',max_digits=10, decimal_places=2, default=0)
    estilo = models.CharField(blank=True, max_length=100)
    order = models.IntegerField('orden', default=0)

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        ordering = ['-created']


    def __str__(self):
        return str(self.id)
