from rest_framework.viewsets import ModelViewSet
from .models import Home
from .serializers import HomeSerializer


# Create your views here.
class HomeViewSet(ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
