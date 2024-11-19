from django.shortcuts import render, redirect
from django.http import JsonResponse
from dbms_service.models import User, Patient, Doctor
import json

# 1. Patient Views

def create_patient_view(request):


    if request.method == 'GET':
        return render(request, 'frontend_service/index.html')


    print('here --' ,request)
    if request.method == 'POST':
        patient_data = request.POST
        patient_data = request.POST.dict()  # Convert QueryDict to a regular dictionary
        patient_data_json = json.dumps(patient_data, indent=4)  # Convert to JSON formatted string

        # Log or print the patient data for debugging
        print("Patient Data (JSON):", patient_data_json)  # This will print to the console
        return render(request, 'frontend_service/index.html')

    
        # Extracting the User-specific fields (first_name, middle_name, last_name, and nat_id)
        user_fields = {
            'nat_id': patient_data.get('nat_id'),
            'first_name': patient_data.get('first_name'),
            'middle_name': patient_data.get('middle_name'),
            'last_name': patient_data.get('last_name'),
        }
        
        # Extracting the Patient-specific fields
        patient_fields = {
            'street': patient_data.get('street'),
            'region': patient_data.get('region'),
            'city': patient_data.get('city'),
            'phone_number': patient_data.get('phone_number'),
            'email': patient_data.get('email'),
            'gender': patient_data.get('gender'),
            'dob': patient_data.get('dob'),
            'blood_type': patient_data.get('blood_type'),
            'height': patient_data.get('height'),
            'weight': patient_data.get('weight'),
        }

        try:
            # Create the patient by calling the create_patient method
            patient = Patient.create_patient(**user_fields, **patient_fields)
            return JsonResponse({'message': 'Patient created successfully', 'patient': patient.first_name})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'frontend_service/index.html')

def retrieve_patient_view(request, nat_id):
    try:
        patient = Patient.retrieve_patient(nat_id)
        if isinstance(patient, Patient):
            return render(request, 'patient_detail.html', {'patient': patient})
        else:
            return JsonResponse({'error': patient}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def update_patient_view(request, nat_id):
    if request.method == 'POST':
        update_data = request.POST
        
        # Extracting the User-specific fields (first_name, middle_name, last_name)
        user_fields = {
            'first_name': update_data.get('first_name'),
            'middle_name': update_data.get('middle_name'),
            'last_name': update_data.get('last_name'),
        }
        
        # Extracting the Patient-specific fields
        patient_fields = {
            'street': update_data.get('street'),
            'region': update_data.get('region'),
            'city': update_data.get('city'),
            'phone_number': update_data.get('phone_number'),
            'email': update_data.get('email'),
            'gender': update_data.get('gender'),
            'dob': update_data.get('dob'),
            'blood_type': update_data.get('blood_type'),
            'height': update_data.get('height'),
            'weight': update_data.get('weight'),
        }

        try:
            result = Patient.update_patient(nat_id, **user_fields, **patient_fields)
            return JsonResponse({'message': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'update_patient.html')

def delete_patient_view(request, nat_id):
    try:
        result = Patient.delete_patient(nat_id)
        return JsonResponse({'message': result})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    



































# 2. Doctor Views

def create_doctor_view(request):
    if request.method == 'POST':
        doctor_data = request.POST
        try:
            doctor = Doctor.objects.create_doctor(**doctor_data)
            return JsonResponse({'message': 'Doctor created successfully', 'doctor': doctor.first_name})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'create_doctor.html')

def retrieve_doctor_view(request, nat_id):
    try:
        doctor = Doctor.objects.retrieve_doctor(nat_id)
        if isinstance(doctor, Doctor):
            return render(request, 'doctor_detail.html', {'doctor': doctor})
        else:
            return JsonResponse({'error': doctor}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

def update_doctor_view(request, nat_id):
    if request.method == 'POST':
        update_data = request.POST
        try:
            result = Doctor.objects.update_doctor(nat_id, **update_data)
            return JsonResponse({'message': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'update_doctor.html')

def delete_doctor_view(request, nat_id):
    try:
        result = Doctor.objects.delete_doctor(nat_id)
        return JsonResponse({'message': result})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

