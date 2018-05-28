from .views import healthcheck, get_all_brothers

from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'brothers', views.BrotherViewSet)



urlpatterns = [
    url(r'healthcheck$', healthcheck, name='healthcheck'),
    url(r'allbrothers', get_all_brothers, name='return all brothers'),
]