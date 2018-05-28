from rest_framework import serializers

from icecoldportal.apps.api.models import Brother


class BrotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brother
        # fields = ('first_name', 'last_name', 'crossing_date')
        fields = '__all__'
