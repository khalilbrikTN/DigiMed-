from django.urls import path
from . import views

# Access the initialized service
pmrm_service = views.pmrm_service

urlpatterns = [
    # MedicalConditions Endpoints
    path('medical_conditions', pmrm_service.medical_conditions.create_medical_condition, name='create_medical_condition'),
    path('medical_conditions/<str:patient_nat_id>/<str:med_condition>', pmrm_service.medical_conditions.retrieve_medical_condition, name='retrieve_medical_condition'),
    path('medical_conditions/<str:patient_nat_id>/<str:med_condition>', pmrm_service.medical_conditions.edit_medical_condition, name='edit_medical_condition'),
    path('medical_conditions/<str:patient_nat_id>/<str:med_condition>', pmrm_service.medical_conditions.delete_medical_condition, name='delete_medical_condition'),

    # MedicalTests Endpoints
    path('medical_tests', pmrm_service.medical_tests.create_medical_test, name='create_medical_test'),
    path('medical_tests/<str:patient_nat_id>/<int:test_id>', pmrm_service.medical_tests.retrieve_medical_test, name='retrieve_medical_test'),
    path('medical_tests/<str:patient_nat_id>/<int:test_id>', pmrm_service.medical_tests.edit_medical_test, name='edit_medical_test'),
    path('medical_tests/<str:patient_nat_id>/<int:test_id>', pmrm_service.medical_tests.delete_medical_test, name='delete_medical_test'),

    # TreatedBy Endpoints
    path('treated_by', pmrm_service.treated_by.create_treated_by, name='create_treated_by'),
    path('treated_by/<str:patient_nat_id>/<str:doctor_nat_id>', pmrm_service.treated_by.retrieve_treated_by, name='retrieve_treated_by'),
    path('treated_by/<str:patient_nat_id>/<str:doctor_nat_id>', pmrm_service.treated_by.edit_treated_by, name='edit_treated_by'),
    path('treated_by/<str:patient_nat_id>/<str:doctor_nat_id>', pmrm_service.treated_by.delete_treated_by, name='delete_treated_by'),
]
