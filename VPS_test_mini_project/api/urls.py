from django.urls import include, path
from rest_framework import routers


from api.views import VPSViewSet

router = routers.DefaultRouter()
router.register(r'vps', VPSViewSet, basename='vps')

urlpatterns = [
    path('', include(router.urls)),
]
