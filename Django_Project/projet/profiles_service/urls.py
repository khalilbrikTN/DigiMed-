from django.urls import path
from .views import PatientView 


urlpatterns = [
    path('patient/', PatientView.create_patient_view, name='create_patient'),
    path('doctor/', PatientView.create_doctor_view, name='create_doctor'),
    path('nurse/', PatientView.create_doctor_view, name='create_nurse'),
    path('pharmacist/', PatientView.create_doctor_view, name='create_pharmacist'),
]



