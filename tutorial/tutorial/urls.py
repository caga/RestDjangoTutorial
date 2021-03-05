from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from django.contrib import admin
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

 
urlpatterns = [
    path ('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('snippets.urls')),
    path('admin/',admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('restler/semalar/arayuz/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
 ]
