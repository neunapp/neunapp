# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# third-party
from model_utils.models import TimeStampedModel



class Product(TimeStampedModel):

    name = models.CharField('nombre', max_length=30)
    description_show = models.CharField('descripcion corta', max_length=100)
    image = models.ImageField('imagen')
    slogan = models.ImageField('slogan')
    video = models.CharField('video', max_length= 200)
    resume = models.CharField('resumen', max_length= 300)
    visit = models.IntegerField('visita')

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['-created']

    def __str__(self):
        return self.name



class Citation(TimeStampedModel):

    product = models.ForeignKey(Product, verbose_name='producto', blank=True, null=True)
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



class ProductSolicitude(TimeStampedModel):

    producto = models.ForeignKey(Product, verbose_name='producto')
    email = models.EmailField('email')
    phone = models.CharField('celular', max_length=12)

    class Meta:
        verbose_name = 'producto solicitud'
        verbose_name_plural = 'producto solicitudes'
        ordering = ['-created']

    def __str__(self):

       return self.producto.name



class ProductPropertys(TimeStampedModel):

    producto = models.ForeignKey(Product, verbose_name='producto')
    title = models.CharField('titulo' , max_length=80)
    description = models.CharField('descripcion', max_length=300)
    icon = models.ImageField('Icono')

    class Meta:
        verbose_name = 'propiedad producto'
        verbose_name_plural = 'propiedad productos'
        ordering = ['-created']

    def __str__(self):

       return self.title

