
from django.db import models

class BlogManager(models.Manager):
    """procedimiento para tabla blog"""

    def search_blog(self, name):
        """funcion que devuelve blogs mas visitados"""

        #filtramos por nombre
        return self.filter(
            published = True,
            title__icontains = name,
        ).order_by('-views')[:20]


    def search_blog_by_category(self, slug):
        #filtramos por nombre blog
        return self.filter(
            published=True,
            category__slug = slug,
        ).order_by('-views')[:20]

    def filter_blog_by_master_category(self, slug, name):
        #filtramos por nombre blog
        return self.filter(
            published=True,
            category__master_category__slug = slug,
            title__icontains = name,
        ).order_by('-views')


class CategoryManager(models.Manager):
    """procedimiento para tabla category"""

    def list_category(self):
        return self.order_by('-name')
