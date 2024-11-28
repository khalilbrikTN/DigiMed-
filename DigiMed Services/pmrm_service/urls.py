from django.urls import path
from .views import MedicalConditionView, MedicalTestView, TreatedByView

urlpatterns = [
    # Medical Conditions URLs
    path('medical_conditions/', MedicalConditionView.as_view(), name='create_medical_condition'),
    path('medical_conditions/<str:patient_nat_id>/<str:med_condition>/', MedicalConditionView.as_view(), name='medical_condition_detail'),

    # Medical Tests URLs
    path('medical_tests/', MedicalTestView.as_view(), name='create_medical_test'),
    path('medical_tests/<str:patient_nat_id>/<str:test_id>/', MedicalTestView.as_view(), name='medical_test_detail'),

    # Treated By URLs
    path('treated_by/', TreatedByView.as_view(), name='create_treated_by'),
    path('treated_by/<str:patient_nat_id>/<str:doctor_nat_id>/', TreatedByView.as_view(), name='treated_by_detail'),
]