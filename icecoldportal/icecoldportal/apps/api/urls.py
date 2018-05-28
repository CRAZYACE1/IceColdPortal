from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from .views import all_brothers, create_brother, healthcheck
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'allbrothers$', all_brothers),
    url(r'createbrother$', create_brother),
    url(r'healthcheck$', healthcheck),
]