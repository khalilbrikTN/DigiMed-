# frontend/urls.py
from django.urls import path
from .views import main_view, contact_view, about_view, login_view, privacy_view


urlpatterns = [
    path('', main_view, name='main'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('privacy/', privacy_view, name='privacy'),
    path('login/', login_view, name='login'),
]