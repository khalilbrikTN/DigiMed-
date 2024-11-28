
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from dbms_service.models import User, Doctor, Patient



# Main Apis
def user_home_view(request):
    return render(request, 'frontend_service/user_home.html')


def manage_view(request):
    return render(request, 'frontend_service/user_manage.html')

def scheduling_view(request):
    return render(request, 'frontend_service/scheduling.html')

def appointments_view(request):
    return render(request, 'frontend_service/appointements.html')

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
    if request.method == "POST":
        return user_home_view(request)

        user_id = request.POST.get("user_id")
        password = request.POST.get("password")
        role = request.POST.get("role")
        try:
            user = User.objects.get(nat_id=user_id)
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('login') 
        

    
        if role == 'patient':
            try:
                patient = Patient.objects.get(user=user)
                login(request, user)  
                return redirect('userpage') 
            except Patient.DoesNotExist:
                messages.error(request, "You are not a registered patient.")
                return redirect('login')
        
        elif role == 'doctor':
            try:
                doctor = Doctor.objects.get(user=user)
                login(request, user)  
                return redirect('doctor_dashboard') 
            except Doctor.DoesNotExist:
                messages.error(request, "You are not a registered doctor.")
                return redirect('login')
        
        else:
            messages.error(request, "Invalid role selected.")
            return redirect('login')

    return render(request, 'frontend_service/login.html')

