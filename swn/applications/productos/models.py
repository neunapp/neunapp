# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible

# third-party
from datetime import timedelta, datetime
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

# third-party
from model_utils.models import TimeStampedModel
#
from .managers import ProductManager


@python_2_unicode_compatible
class Product(TimeStampedModel):
    """ modelo para Productos """

    name = models.CharField('nombre', max_length=200)
    description_show = models.TextField(blank=True)
    image = models.ImageField('imagen')
    slogan = models.CharField(blank=True, max_length=200)
    video = models.URLField(blank=True)
    content = RichTextUploadingField('resumen')
    slug = models.SlugField(editable=False, max_length=250)
    visit = models.IntegerField('visita')
    published = models.BooleanField(default=False)

    objects = ProductManager()

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['-created']

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        #actualizamos video
        video = self.video.split('/')
        if len(video) == 4:
            self.video = "https://www.youtube.com/embed/"+video[3]
        else:
            print 'no se guardo nuevo video'

        #
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.name, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.name, str(seconds))

        self.slug = slugify(slug_unique)
        super(Product, self).save(*args, **kwargs)



@python_2_unicode_compatible
class Citation(TimeStampedModel):
    """ modelo para registrar cita """

    product = models.ForeignKey(
        Product,
        verbose_name='producto_citacion',
        blank=True,
        null=True
    )
    email = models.EmailField('email')
    phone = models.CharField('Celular', max_length=30)
    address = models.CharField('Direccion', max_length=50)
    name = models.CharField('nombre', max_length=40)
    hour_atention = models.CharField('hora de atencion', max_length= 40)
    day_atention = models.CharField('dia de atencion', max_length= 40)
    messagge = models.TextField('mensaje',blank=True)

    class Meta:
        verbose_name = 'citacion'
        verbose_name_plural = 'citaciones'
        ordering = ['-created']

    def __str__(self):

        return self.email



@python_2_unicode_compatible
class ProductSolicitude(TimeStampedModel):
    """ modelo para registrar soliciutd e un producto """

    producto = models.ForeignKey(
        Product,
        verbose_name='producto_solicitud',
        blank=True,
        null=True
    )
    email = models.EmailField('email')
    phone = models.CharField('celular', max_length=30)

    class Meta:
        verbose_name = 'producto solicitud'
        verbose_name_plural = 'producto solicitudes'
        ordering = ['-created']

    def __str__(self):
       return self.producto.name



@python_2_unicode_compatible
class ProductPropertys(TimeStampedModel):
    """" modelo para registrar propiedades de un producto """

    producto = models.ForeignKey(
        Product,
        verbose_name='producto_propiedades'
    )
    title = models.CharField('titulo', max_length=60)
    description = models.CharField('descripcion', max_length=300)
    icon = models.CharField('icono',blank=True, max_length=30)

    class Meta:
        verbose_name = 'propiedad producto'
        verbose_name_plural = 'propiedad productos'
        ordering = ['-created']

    def __str__(self):

       return self.producto.name
