from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()

urlpatterns = [
    url(r'^auth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^docs/', include_docs_urls(title='Orgs API')),
]

urlpatterns += router.urls
