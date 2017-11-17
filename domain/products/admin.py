from django.contrib import admin

from domain.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
