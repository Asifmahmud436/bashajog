from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OwnerDataByUserIDView,OwnerRegistrationAPIView,OwnerViewSet,activate



router = DefaultRouter()
router.register('list', OwnerViewSet)
urlpatterns = [
    path('', include(router.urls)),

    path('register/', OwnerRegistrationAPIView.as_view(), name='owner_register'),
    path('active/<user_id>/<token>/', activate, name='owner_account_activate'),

    path('by_user_id/', OwnerDataByUserIDView.as_view(), name='owner_by_user_id'),
]