from django.urls import path
from .import views
from django.urls import path, include
from .views import GoogleLoginView

urlpatterns = [
    path('user/',views.UserDetailView.as_view(),name='user-detail'),
    path('login/',views.LoginAPIView.as_view(),name='user-login'),
    path('logout/',views.LogoutAPIView.as_view(),name='user-logout'),
    # for google auth
    path('google/', GoogleLoginView.as_view(), name='google_login'),
    path('', include('allauth.urls')),
]
