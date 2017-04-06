# Create your views here.
from django.core.urlresolvers import reverse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class APIList(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({
            'conferences': request.build_absolute_uri(reverse('conferences-list')),
        })
