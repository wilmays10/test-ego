from django.urls import path, include
from rest_framework import routers
from car.api.views import GroupViewSet, VersionViewSet


router = routers.DefaultRouter()
router.register('modelos', GroupViewSet, basename='cars.api.modelos')
router.register('versiones', VersionViewSet, basename='cars.api.versiones')


urlpatterns = [
    path('', include(router.urls)),
]