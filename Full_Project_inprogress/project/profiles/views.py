
# BY : MOHAMED KHALIL BRIK

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import search_doctors, search_patients
from .serializers import DoctorSerializer, PatientSerializer
from rest_framework.pagination import PageNumberPagination

class SearchDoctorsView(APIView):
    """
    Class-based view for searching doctors with various filters.
    """
    def get(self, request, *args, **kwargs):
        # Get filter parameters from the query string
        specialty = request.GET.get('specialty')
        sub_specialty = request.GET.get('sub_specialty')
        location = request.GET.get('location')

        # Perform doctor search based on the filters
        doctors = search_doctors(specialty=specialty, sub_specialty=sub_specialty, location=location)

        # Implement pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # You can adjust the page size as needed
        result_page = paginator.paginate_queryset(doctors, request)
        
        # Serialize the data
        serializer = DoctorSerializer(result_page, many=True)
        
        # Return paginated response
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        If needed, you can add a POST method for more complex searches or saving filters.
        """
        # Handling the search request with filters in the body (optional)
        specialty = request.data.get('specialty')
        sub_specialty = request.data.get('sub_specialty')
        location = request.data.get('location')

        doctors = search_doctors(specialty=specialty, sub_specialty=sub_specialty, location=location)

        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Additional methods for sorting or advanced search can be added if needed.
    def filter_by_name(self, query, name):
        """
        Example of how to filter by name or full name if necessary
        """
        return query.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))


class SearchPatientsView(APIView):
    """
    Class-based view for searching patients with various filters.
    """
    def get(self, request, *args, **kwargs):
        # Get filter parameters from the query string
        city = request.GET.get('city')
        blood_type = request.GET.get('blood_type')
        age = request.GET.get('age')
        gender = request.GET.get('gender')

        # Perform patient search based on the filters
        patients = search_patients(city=city, blood_type=blood_type, age=age, gender=gender)

        # Implement pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10  # You can adjust the page size as needed
        result_page = paginator.paginate_queryset(patients, request)

        # Serialize the data
        serializer = PatientSerializer(result_page, many=True)

        # Return paginated response
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Similar to the doctors, you can also handle POST requests for complex search parameters.
        """
        # Handling the search request with filters in the body (optional)
        city = request.data.get('city')
        blood_type = request.data.get('blood_type')
        age = request.data.get('age')
        gender = request.data.get('gender')

        patients = search_patients(city=city, blood_type=blood_type, age=age, gender=gender)

        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Additional methods for sorting or filtering patients by more complex criteria can be added.
    def filter_by_age_range(self, query, min_age, max_age):
        """
        Example method to filter patients by a specific age range
        """
        return query.filter(age__gte=min_age, age__lte=max_age)
