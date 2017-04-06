from django.conf.urls import url
from .views import APIList

urlpatterns = [
    url(r'^$', APIList.as_view()),
]
