from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TenantDataByUserIDView,TenantRegistrationAPIView,TenantViewSet,activate



router = DefaultRouter()
router.register('list', TenantViewSet)
urlpatterns = [
    path('', include(router.urls)),

    path('register/', TenantRegistrationAPIView.as_view(), name='tenant_register'),
    path('active/<user_id>/<token>/', activate, name='tenant_account_activate'),

    path('by_user_id/', TenantDataByUserIDView.as_view(), name='tenant_by_user_id'),
]