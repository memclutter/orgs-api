from django_filters import rest_framework as filters

from domain.orgs.models import Article


class ArticleByOrganizationFilter(filters.FilterSet):
    price_from = filters.NumberFilter(name="price", lookup_expr='gte')
    price_to = filters.NumberFilter(name="price", lookup_expr='lte')

    class Meta:
        model = Article
        fields = ['price_from', 'price_to']
