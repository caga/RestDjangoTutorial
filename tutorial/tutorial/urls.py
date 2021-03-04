from django.urls import include, path
from rest_framework import routers
from quickstart import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register (r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
 
 # Wire up our UPI using atuomatic URL routing
 # Additionall, we inclid login URLs for teh browsable UPI.

urlpatterns = [
    path('',include(router.urls)),
    path ('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('snippets.urls')),
    path('admin/',admin.site.urls),
    # path('api-auth/', include('rest_framework')),
 ]
