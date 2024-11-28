# dbms_service/urls.py

from django.urls import path, include
from .views import (
    PatientViewSet, MedicalConditionList, MedicalConditionDetail,
    MedicalTestList, MedicalTestDetail, PatientCreateView,
    # Include other views as needed
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')

urlpatterns = [
    path('', include(router.urls)),
    # MedicalCondition endpoints
    path(
        'medicalConditions/',
        MedicalConditionList.as_view(),
        name='medicalcondition-list'
    ),
    path(
        'medicalConditions/<str:patient_nat_id>/<str:med_condition>/',
        MedicalConditionDetail.as_view(),
        name='medicalcondition-detail'
    ),
    # MedicalTest endpoints
    path(
        'medicalTests/',
        MedicalTestList.as_view(),
        name='medicaltest-list'
    ),
    path(
        'medicalTests/<str:patient_nat_id>/<int:test_id>/',
        MedicalTestDetail.as_view(),
        name='medicaltest-detail'
    ),
    # Patient creation endpoint
    path(
        'patients/create/',
        PatientCreateView.as_view(),
        name='patient-create'
    ),
    # Add other custom endpoints
]
