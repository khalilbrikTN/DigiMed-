# dbms_service/views.py

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    Patient, MedicalCondition, MedicalTest, TreatmentAssignment,
    Appointment, Prescription, Medicine, Referral, ORG, ORGLocation,
    DoctorWorkingDays
)
from .serializers import (
    PatientSerializer, MedicalConditionSerializer, MedicalTestSerializer,
    TreatmentAssignmentSerializer, AppointmentSerializer, PrescriptionSerializer,
    MedicineSerializer, ReferralSerializer, ORGSerializer, ORGLocationSerializer,
    DoctorWorkingDaysSerializer
)
from django.shortcuts import get_object_or_404

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class MedicalConditionList(APIView):
    def post(self, request):
        serializer = MedicalConditionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            print("Serializer errors (MedicalCondition POST):", serializer.errors)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

class MedicalConditionDetail(APIView):
    def get_object(self, patient_nat_id, med_condition):
        patient = get_object_or_404(Patient, nat_id=patient_nat_id)
        return get_object_or_404(
            MedicalCondition,
            patient=patient,
            med_condition=med_condition
        )

    def get(self, request, patient_nat_id, med_condition):
        medical_condition = self.get_object(patient_nat_id, med_condition)
        serializer = MedicalConditionSerializer(medical_condition)
        return Response(serializer.data)

    def put(self, request, patient_nat_id, med_condition):
        medical_condition = self.get_object(patient_nat_id, med_condition)
        serializer = MedicalConditionSerializer(
            medical_condition, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print("Serializer errors (MedicalCondition PUT):", serializer.errors)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, patient_nat_id, med_condition):
        medical_condition = self.get_object(patient_nat_id, med_condition)
        medical_condition.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MedicalTestList(APIView):
    def post(self, request):
        serializer = MedicalTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            print("Serializer errors (MedicalTest POST):", serializer.errors)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

class MedicalTestDetail(APIView):
    def get_object(self, patient_nat_id, test_id):
        patient = get_object_or_404(Patient, nat_id=patient_nat_id)
        return get_object_or_404(
            MedicalTest,
            patient=patient,
            test_id=test_id
        )

    def get(self, request, patient_nat_id, test_id):
        medical_test = self.get_object(patient_nat_id, test_id)
        serializer = MedicalTestSerializer(medical_test)
        return Response(serializer.data)

    def put(self, request, patient_nat_id, test_id):
        medical_test = self.get_object(patient_nat_id, test_id)
        serializer = MedicalTestSerializer(
            medical_test, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print("Serializer errors (MedicalTest PUT):", serializer.errors)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, patient_nat_id, test_id):
        medical_test = self.get_object(patient_nat_id, test_id)
        medical_test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PatientCreateView(APIView):
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        else:
            print("Serializer errors (Patient POST):", serializer.errors)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )