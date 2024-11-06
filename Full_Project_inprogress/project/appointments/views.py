from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from .utils import book_appointment  # Assuming the function is in utils.py

def book_appointment_view(request):
    doctor_id = request.POST.get("doctor_id")
    patient_id = request.POST.get("patient_id")
    org_num = request.POST.get("org_num")
    appointment_datetime_str = request.POST.get("appointment_datetime")
    
    # Convert appointment date string to datetime object
    appointment_datetime = datetime.strptime(appointment_datetime_str, "%Y-%m-%d %H:%M:%S")
    
    result_message = book_appointment(doctor_id, patient_id, org_num, appointment_datetime)
    return JsonResponse({"message": result_message})
