from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
