from django.urls import path
from .import views

urlpatterns = [
    path('user/',views.UserDetailView.as_view(),name='user-detail'),
    path('login/',views.LoginAPIView.as_view(),name='user-login'),
    path('logout/',views.LogoutAPIView.as_view(),name='user-logout'),
]
