from .views import ActivityViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"", ActivityViewSet, basename="activities")

urlpatterns = router.urls
