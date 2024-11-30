# frontend/urls.py
from django.urls import path
from .views import main_view, contact_view 
from .views import about_view, manage_view, login_view, scheduling_view
from .views import privacy_view, user_home_view, records_view, workingHours_view, appointments_view, book_appointments_view


urlpatterns = [
    path('', main_view, name='main'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('privacy/', privacy_view, name='privacy'),
    path('login/', login_view, name='login'),

    path('userpage/<str:user_id>/', user_home_view, name='userPage'),



    path('records/', records_view, name='records'),
    path('doctorHours/', workingHours_view, name='doctorHours'),
    path('appointments/', appointments_view, name='appointments'),
    path('book-appointment/', book_appointments_view, name='book-appointment'),
    path('scheduling/', scheduling_view, name='scheduling'),
    path('manage/', manage_view, name='manage'),

]