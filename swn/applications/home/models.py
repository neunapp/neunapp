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




