from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhaseViewSet, CardViewSet, FieldViewSet

router = DefaultRouter()
router.register(r'phases', PhaseViewSet)
router.register(r'cards', CardViewSet)
router.register(r'fields', FieldViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
