# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# third-party
from model_utils.models import TimeStampedModel
from django.db import models

# Create your models here.
class Suscription(TimeStampedModel):

    email = models.EmailField('email')

    class Meta:
        verbose_name = 'suscripcion'
        verbose_name_plural = 'suscripciones'
        ordering = ['-created']

    def __str__(self):
        return self.email



class Citation(TimeStampedModel):

    email = models.EmailField('email')
    phone = models.CharField('Celular', max_length=12)
    address = models.CharField('Direccion', max_length=30)
    name = models.CharField('nombre', max_length=40)
    hour_atention = models.CharField('hora de atencion', max_length= 15)
    day_atention = models.CharField('dia de atencion', max_length= 15)

    class Meta:
        verbose_name = 'citacion'
        verbose_name_plural = 'citaciones'
        ordering = ['-created']

    def __str__(self):
        return self.name
