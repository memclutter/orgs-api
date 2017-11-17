from django.db import models

from domain.refs.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    category = models.ForeignKey(Category, related_name='products')

    def __str__(self):
        return self.name
