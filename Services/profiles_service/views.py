
# BY : MOHAMED KHALIL BRIK

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import search_doctors, search_patients
from .serializers import DoctorSerializer, PatientSerializer
from rest_framework.pagination import PageNumberPagination

class SearchDoctorsView(APIView):

    def get(self, request, *args, **kwargs):
        specialty = request.GET.get('specialty')
        sub_specialty = request.GET.get('sub_specialty')
        location = request.GET.get('location')

        doctors = search_doctors(specialty=specialty, sub_specialty=sub_specialty, location=location)

        paginator = PageNumberPagination()
        paginator.page_size = 10  
        result_page = paginator.paginate_queryset(doctors, request)
        
        serializer = DoctorSerializer(result_page, many=True)
        
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):

        specialty = request.data.get('specialty')
        sub_specialty = request.data.get('sub_specialty')
        location = request.data.get('location')

        doctors = search_doctors(specialty=specialty, sub_specialty=sub_specialty, location=location)

        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def filter_by_name(self, query, name):
 
        return query.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))


class SearchPatientsView(APIView):

    def get(self, request, *args, **kwargs):
        city = request.GET.get('city')
        blood_type = request.GET.get('blood_type')
        age = request.GET.get('age')
        gender = request.GET.get('gender')

        patients = search_patients(city=city, blood_type=blood_type, age=age, gender=gender)

        paginator = PageNumberPagination()
        paginator.page_size = 10  
        result_page = paginator.paginate_queryset(patients, request)

        serializer = PatientSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        city = request.data.get('city')
        blood_type = request.data.get('blood_type')
        age = request.data.get('age')
        gender = request.data.get('gender')

        patients = search_patients(city=city, blood_type=blood_type, age=age, gender=gender)

        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def filter_by_age_range(self, query, min_age, max_age):

        return query.filter(age__gte=min_age, age__lte=max_age)
