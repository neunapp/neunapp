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

    name = models.CharField('nombre', max_length=60)
    image = models.ImageField('imagen', upload_to='cotizacion')

    class Meta:
        verbose_name = 'cita'
        verbose_name_plural = 'citas'
        ordering = ['-created']

    def __str__(self):
        return self.name



@python_2_unicode_compatible
class RequestQuote(TimeStampedModel):
    """ 
        datamodel RequestQuote
    """
    typequote = models.ForeignKey(TypeQuote, verbose_name='cita')
    email = models.EmailField('email')
    phone = models.CharField('telefono', max_length=12)
    message= models.CharField('mensaje', max_length=300)
    amount = models.IntegerField('monto')
    answer = ArrayField(models.CharField('Respuesta',max_length=7, blank=True))


    class Meta:
        verbose_name = 'cotizacion'
        verbose_name_plural = 'cotizaciones'
        ordering = ['-created']

    def __str__(self):
        return self.email



@python_2_unicode_compatible
class Question(TimeStampedModel):

    typequote = models.ForeignKey(TypeQuote, verbose_name='cita')
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

    question = models.ForeignKey(Question, verbose_name='pregunta')
    image = models.ImageField('imagen', upload_to='cotizacion')

    class Meta:
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'
        ordering = ['-created']


    def __str__(self):
        return self.question






