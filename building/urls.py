from rest_framework.routers import DefaultRouter
from .import views
from django.urls import path,include

router = DefaultRouter()

router.register('list',views.BuildingViewSet)
router.register('unit',views.UnitViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
