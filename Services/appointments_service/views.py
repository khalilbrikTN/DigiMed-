from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse
from .utils import AppointmentManager  


appointment_manager = AppointmentManager()



def book_appointment_view(request):
    doctor_id = request.POST.get("doctor_id")
    patient_id = request.POST.get("patient_id")
    org_num = request.POST.get("org_num")
    appointment_datetime_str = request.POST.get("appointment_datetime")

    try:
        appointment_datetime = datetime.strptime(appointment_datetime_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return JsonResponse({"message": "Error: Invalid date format. Use YYYY-MM-DD HH:MM:SS."})

    result_message = appointment_manager.book_appointment(doctor_id, patient_id, org_num, appointment_datetime)
    return JsonResponse({"message": result_message})


def cancel_appointment_view(request):
    appointment_id = request.POST.get("appointment_id")

    if not appointment_id:
        return JsonResponse({"message": "Error: appointment_id is required."})

    result_message = appointment_manager.cancel_appointment(appointment_id)
    return JsonResponse({"message": result_message})
