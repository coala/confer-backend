from rest_framework import viewsets

from .models import Conference
from .serializers import ConferenceExtendedSerializer, ConferenceSerializer


class ConferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ConferenceSerializer
    queryset = Conference.objects.all()
    filter_fields = ('name', 'slug', 'category')
    search_fields = ('name',)

    def get_queryset(self):
        queryset = Conference.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """

        if self.action in ['list', 'retrieve']:
            extended_serializer_parameter = self.request.query_params.get('extended')
            if extended_serializer_parameter:
                extended_serializer = extended_serializer_parameter.lower() in ['1', 'true', 'yes', 'y']
                if extended_serializer:
                    return ConferenceExtendedSerializer(*args, **kwargs)

        return super(ConferenceViewSet, self).get_serializer(*args, **kwargs)
