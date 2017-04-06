from rest_framework import viewsets

from .models import Conference
from .serializers import ConferenceSerializer


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
