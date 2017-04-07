from rest_framework import serializers

from .models import Conference


class ConferenceSerializer(serializers.ModelSerializer):
    resource_link = serializers.CharField(required=False)

    class Meta:
        model = Conference
        # fields = ['name', 'source_url', 'website', 'start', 'end', 'cfp_closes', 'finaid_closes', 'tags']
        fields = '__all__'


class ConferenceExtendedSerializer(ConferenceSerializer):
    class Meta:
        model = Conference
        fields = '__all__'
        depth = 2
