from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from . import views

router = DefaultRouter()
router.register(r'organizations/(?P<district>\d+)', views.OrganizationByDistrictViewSet)

urlpatterns = [
    url(r'^auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^docs/', include_docs_urls(title='Orgs API')),
]

urlpatterns += router.urls
