from django.urls import path
from .views import create_patient_view, create_doctor_view


urlpatterns = [
    path('patient/', create_patient_view, name='create_patient'),
    path('doctor/', create_doctor_view, name='create_doctor'),
    path('nurse/', create_doctor_view, name='create_nurse'),
    path('pharmacist/', create_doctor_view, name='create_pharmacist'),
]



