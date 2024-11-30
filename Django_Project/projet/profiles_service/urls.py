from django.urls import path
from .views import PatientView, DoctorView


urlpatterns = [
    path('patient/create', PatientView.create_patient, name='create_patient'),
    path('patient/retrieve', PatientView.retrieve_patient, name='retrieve_patient'),
    path('patient/update', PatientView.update_patient, name='update_patient'),
    path('patient/delete', PatientView.delete_patient, name='delete_patient'),


    path('doctor/create', DoctorView.create_doctor, name='create_doctor'),
    path('doctor/retrieve', DoctorView.retrieve_doctor, name='retrieve_doctor'),
    path('doctor/update', DoctorView.update_doctor, name='update_doctor'),
    path('doctor/delete', DoctorView.delete_doctor, name='delete_doctor'),


    path('nurse/', DoctorView.create_doctor, name='create_nurse'),
    path('pharmacist/', PatientView.create_patient, name='create_pharmacist'),
]



