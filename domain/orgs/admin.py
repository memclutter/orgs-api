from django.contrib import admin

from domain.orgs.models import Network, Organization, Article


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
