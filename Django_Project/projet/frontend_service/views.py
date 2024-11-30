
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import json
from dbms_service.models import User, Doctor, Patient
from django.urls import reverse



# Main Apis
def user_home_view(request, user_id):
    patient = get_object_or_404(Patient, nat_id=user_id)

    context = {'name' : patient.first_name }
 
    return render(request, 'frontend_service/user_home.html', context)

def manage_view(request):
    return render(request, 'frontend_service/user_manage.html')

def scheduling_view(request):
    return render(request, 'frontend_service/scheduling.html')

def appointments_view(request):
    return render(request, 'frontend_service/appointements.html')

def book_appointments_view(request):
    return render(request, 'frontend_service/book-appointments.html')

def workingHours_view(request):
    return render(request, 'frontend_service/doctorhours.html')

def records_view(request):
    return render(request, 'frontend_service/records.html')

def main_view(request):
    return render(request, 'frontend_service/main.html')

def about_view(request):
    return render(request, 'frontend_service/about.html')

def contact_view(request):
    return render(request, 'frontend_service/contact.html')

def privacy_view(request):
    return render(request, 'frontend_service/privacy.html')

def login_view(request):
    context = {}
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        role = request.POST.get("role")

        context['user_id'] = user_id
        context['role'] = role

        if role == "doctor":
            response = Doctor.login_doctor(nat_id=user_id, password=password)
        elif role == "patient":
            response = Patient.login_patient(nat_id=user_id, password=password)
            print(response)
        else:
            return render(request, "frontend_service/login.html", {"error": "Invalid role selected"})

        if 'error' in response:
            return render(request, "frontend_service/login.html", {"error": response['error']})
        else:
            return  redirect(reverse('userPage', kwargs={'user_id': user_id}))

    return render(request, "frontend_service/login.html")

