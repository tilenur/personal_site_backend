from rest_framework.routers import DefaultRouter
from .views import HomeViewSet

router = DefaultRouter()

router.register(r"", HomeViewSet, basename="home")

urlpatterns = router.urls
