from rest_framework.viewsets import ModelViewSet

from apps.activities.models import Activity
from apps.activities.serializers import (
    ActivitySerializer,
)


# Create your views here.
class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
