from rest_framework import generics
from .serializers import NewsSerializer
from .models import News
from rest_framework.response import Response

# Create your views here.
class NewsViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows news to be viewed or edited.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data)