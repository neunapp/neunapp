# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

#django
from django.db import models
from django.conf import settings
# Create your models here.


class Tag(TimeStampedModel):
    """django data model tag"""

    name = models.CharField('tag', max_length=20)


class Category(TimeStampedModel):
    """django data model categoria"""

    name = models.CharField('nombre', max_length=30)


class Blog(TimeStampedModel):
    """Django data model Blog"""

    title = models.CharField('titulo', max_length=200)
    description = models.TextField('descripcion')
    content = RichTextUploadingField('contenido')
    category = models.ForeignKey(Category, verbose_name='categoria')
    image = models.ImageField(upload_to='blog', verbose_name='imagen')
    slug = models.SlugField(editable=False, max_length=200)
    views = models.PositiveIntegerField('vistas', default=0, editable=False)
    tag = models.ManyToManyField(Tag, verbose_name='tag')
    published = models.BooleanField('publicado', default='false')
    score = models.PositiveIntegerField('puntuacion', default=0, editable=False)
    author = models.CharField('autor', max_length=200)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_Blog'
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='modified_Blog'
    )


class Subscription(TimeStampedModel):
    """django data model suscripcion"""

    email = models.EmailField('email')






class Commentary(TimeStampedModel):
    """django data model comentario"""

    blog = models.ForeignKey(
        Blog,
        verbose_name='blog'
    )
    description = models.CharField(
        'descripcion',
        max_length=300
    )
    email = models.EmailField('email')
    nick = models.CharField('apodo', max_length=30)