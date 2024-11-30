from django.urls import path
from django.shortcuts import render
from .views import MedicalConditionView, home, MedicalTestView, TreatedByView, medical_conditions_page, medical_tests_page, treated_by_page

urlpatterns = [
    # Medical Conditions URLs
    path('', home, name='home'),  # Homepage
    path('medical_conditions/', MedicalConditionView.as_view(), name='medical_conditions'),
    path('medical_conditions/<str:patient_nat_id>/<str:med_condition>/', MedicalConditionView.as_view(), name='medical_condition_detail'),

    # Medical Tests URLs
    path('medical_tests/', MedicalTestView.as_view(), name='medical_tests'),
    path('medical_tests/<str:patient_nat_id>/<str:test_id>/', MedicalTestView.as_view(), name='medical_test_detail'),

    # Treated By URLs
    path('treated_by/', TreatedByView.as_view(), name='treated_by'),
    path('treated_by/<str:patient_nat_id>/<str:doctor_nat_id>/', TreatedByView.as_view(), name='treated_by_detail'),

    # Medical Conditions Page
    path('medical_conditions_page/', medical_conditions_page, name='medical_conditions_page'),

    # Medical Tests Page
    path('medical_tests_page/', medical_tests_page, name='medical_tests_page'),
    # Treated By Page
    path('treated_by_page/', treated_by_page, name='treated_by_page'),
]
