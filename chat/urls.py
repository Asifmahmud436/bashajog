from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ChatRoomViewSet

router = DefaultRouter()
router.register('rooms', ChatRoomViewSet, basename='chatroom')

urlpatterns = [
    path('', include(router.urls)),
]