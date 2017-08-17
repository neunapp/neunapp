# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# standard library
from datetime import timedelta, datetime

# third-party
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

#django
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify

#managers
from .managers import BlogManager



@python_2_unicode_compatible
class Tag(TimeStampedModel):
    """django data model tag"""

    name = models.CharField('tag', max_length=20)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['-created']

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Category(TimeStampedModel):
    """django data model categoria"""

    name = models.CharField('nombre', max_length=30)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-created']

    def __str__(self):
        return self.name


@python_2_unicode_compatible
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
    objects = BlogManager()

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.title, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.title, str(seconds))

        self.slug = slugify(slug_unique)
        super(Blog, self).save(*args, **kwargs)



@python_2_unicode_compatible
class Subscription(TimeStampedModel):
    """django data model suscripcion"""

    email = models.EmailField('email')

    class Meta:
        verbose_name = 'subcripcion'
        verbose_name_plural = 'subcripciones'
        ordering = ['-created']

    def __str__(self):
        return self.email


@python_2_unicode_compatible
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

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'comentarios'
        ordering = ['-created']

    def __str__(self):
        return self.nick