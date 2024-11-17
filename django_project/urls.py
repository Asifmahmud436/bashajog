from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# for swagger ui
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

schema_view = get_schema_view(
    openapi.Info(
        title="BashaBhara",
        default_version='v1',
        description="Easily rent and give rent to homes. Renting made easy and safe for everyone.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="safaandsafa4@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('owners/',include('owners.urls')),
    path('tenants/',include('tenants.urls')),
    path('building/',include('building.urls')),
    path('social-auth/',include('social_django.urls',namespace='social')),
    # path('unit/',include('building.urls')),
    path('booking/',include('booking.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)