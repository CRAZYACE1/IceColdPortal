from django.contrib.auth.models import User, Group
from rest_framework import serializers


class BrotherSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model = Group
        fields = ('url', 'name')