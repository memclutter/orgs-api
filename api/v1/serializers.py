from rest_framework import serializers

from domain.orgs.models import Organization, Network, Article
from domain.products.models import Product
from domain.refs.models import District, Category


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = District
        fields = ('id', 'name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class OrganizationNetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Network
        fields = ('id', 'name',)


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    network = OrganizationNetworkSerializer(many=False, read_only=True)
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('id', 'name', 'description', 'network', 'districts')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'category')


class OrganizationArticleSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductSerializer(many=False, read_only=True)
    organization = OrganizationSerializer(many=False, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'product', 'organization')
