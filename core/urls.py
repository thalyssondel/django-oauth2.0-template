from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # App
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # Auth
    path('api/auth/', include('dj_rest_auth.urls')), 
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')), 

    # Docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]