from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors137081ViewSet

router = DefaultRouter()
router.register(
    "testconnectors137081", Testconnectors137081ViewSet, basename="testconnectors137081"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
