
from django.db import models

class ProductManager(models.Manager):
    """procedimiento para tabla blog"""

    def principal_product(self):
        """funcion que devuelve productos principales"""

        #filtramos por nombre
        return self.filter(
            published = True,
        ).order_by('visit')[:4]
