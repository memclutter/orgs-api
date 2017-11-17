from django.db import models

from domain.products.models import Product
from domain.refs.models import District


class Network(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    network = models.ForeignKey(Network, related_name='organizations')
    districts = models.ManyToManyField(District, related_name='organizations')

    def __str__(self):
        return self.name


class Article(models.Model):
    product = models.ForeignKey(Product, related_name='articles')
    organization = models.ForeignKey(Organization, related_name='articles')
    price = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return '{product} ${price}'.format(product=self.product, price=self.price)
