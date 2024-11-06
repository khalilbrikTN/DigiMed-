

# profiles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('search_doctors/', views.search_doctors_view, name='search_doctors'),
    path('search_patients/', views.search_patients_view, name='search_patients'),
]