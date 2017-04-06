from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .rest import ConferenceViewSet

router = DefaultRouter('conferences')

router.register(r'conferences', ConferenceViewSet, base_name='conferences')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
