from django.contrib import admin
from django.urls import path, include
from profiles_service import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_profile/', include('profiles_service.urls')), 
    path('', include('frontend_service.urls')),
]
