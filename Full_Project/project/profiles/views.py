
# BY : MOHAMED KHALIL BRIK

from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import search_doctors, search_patients
from .serializers import DoctorSerializer, PatientSerializer

@api_view(['GET'])
def search_doctors_view(request):
    specialty = request.GET.get('specialty')
    sub_specialty = request.GET.get('sub_specialty')
    location = request.GET.get('location')

    doctors = search_doctors(specialty=specialty, sub_specialty=sub_specialty, location=location)
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def search_patients_view(request):
    city = request.GET.get('city')
    blood_type = request.GET.get('blood_type')
    age = request.GET.get('age')
    gender = request.GET.get('gender')

    patients = search_patients(city=city, blood_type=blood_type, age=age, gender=gender)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)
