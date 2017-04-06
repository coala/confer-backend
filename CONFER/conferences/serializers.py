from rest_framework import serializers

from .models import Conference


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        # fields = ['name', 'source_url', 'website', 'start', 'end', 'cfp_closes', 'finaid_closes', 'tags']
        fields = '__all__'
