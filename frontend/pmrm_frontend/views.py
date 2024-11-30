from django.http import JsonResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

PMRM_BASE_URL = "http://127.0.0.1:8000/api/pmrm"



from django.shortcuts import render

def home(request):
    """
    Render the homepage with role, nat_id, and doctor_id parameters passed in the query string.
    """
    role = request.GET.get('role')
    nat_id = request.GET.get('nat_id')
    doctor_id = request.GET.get('doctor_id')

    # Validate role and required parameters
    if not role:
        return render(request, 'error.html', {'message': 'Role is required to access this page.'})

    # Pass parameters to the template
    context = {
        'role': role,
        'nat_id': nat_id if role == 'patient' else None,
        'doctor_id': doctor_id if role == 'doctor' else None,
    }
    return render(request, 'home.html', context)


def medical_conditions_page(request):
    """
    Render the Medical Conditions page, passing role, nat_id, and doctor_id from the URL.
    """
    role = request.GET.get('role')
    nat_id = request.GET.get('nat_id')
    doctor_id = request.GET.get('doctor_id')

    # Validate role and required parameters
    if not role:
        return render(request, 'error.html', {'message': 'Role is required to access this page.'})
    if role == 'patient' and not nat_id:
        return render(request, 'error.html', {'message': 'Patient ID is required for patients.'})
    if role == 'doctor' and not doctor_id:
        return render(request, 'error.html', {'message': 'Doctor ID is required for doctors.'})

    # Pass role, nat_id, and doctor_id to the template
    context = {
        'role': role,
        'nat_id': nat_id,
        'doctor_id': doctor_id,
    }
    return render(request, 'medical_conditions.html', context)

@method_decorator(csrf_exempt, name='dispatch')
class MedicalConditionView(View):
    def get(self, request):
        """
        Handles GET requests for fetching all or specific medical conditions.
        Role-based access:
        - Patients can only view their own records.
        - Doctors can view records of any patient.
        - Admins can view all records without restriction.
        """
        user_role = request.user_role  # Extracted from middleware
        user_nat_id = request.user_nat_id  # Extracted from middleware
        doctor_id = request.doctor_id  # Extracted from middleware (optional for doctors)

        patient_nat_id = request.GET.get('patient_nat_id')
        med_condition = request.GET.get('med_condition')

        # Role-based access control
        if user_role == 'patient' and patient_nat_id != user_nat_id:
            return JsonResponse({'error': 'Access denied: Patients can only access their own records'}, status=403)

        try:
            if patient_nat_id and med_condition:
                # Fetch specific medical condition
                url = f"{PMRM_BASE_URL}/medical_conditions/{patient_nat_id}/{med_condition}/"
            else:
                # Fetch all medical conditions
                url = f"{PMRM_BASE_URL}/medical_conditions/"

            response = requests.get(url)
            response.raise_for_status()
            return JsonResponse(response.json(), safe=False, status=response.status_code)

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to fetch medical conditions: {str(e)}"}, status=500)

    def post(self, request):
        """
        Handles POST requests to add or update medical conditions.
        Role-based access:
        - Patients cannot add or update records.
        - Doctors can add or update records for their assigned patients.
        - Admins can add or update any record.
        """
        user_role = request.user_role  # Extracted from middleware
        user_nat_id = request.user_nat_id  # Extracted from middleware
        doctor_id = request.doctor_id  # Extracted from middleware (optional for doctors)

        try:
            method_override = request.POST.get('_method', '').lower()

            if method_override == 'put':
                # Update medical condition
                patient_nat_id = request.POST.get('patient_nat_id')
                med_condition = request.POST.get('med_condition')
                notes = request.POST.get('notes', '')  # Default to empty string

                if not patient_nat_id or not med_condition:
                    return JsonResponse({"error": "Missing required fields for update"}, status=400)

                # Role-based access validation
                if user_role == 'patient':
                    return JsonResponse({'error': 'Access denied: Patients cannot update records'}, status=403)

                if user_role == 'doctor' and patient_nat_id:
                    # Validate doctor-patient relationship
                    relationship_url = f"{PMRM_BASE_URL}/treated_by/{patient_nat_id}/{doctor_id}/"
                    try:
                        relationship_response = requests.get(relationship_url)
                        if relationship_response.status_code != 200:
                            return JsonResponse({'error': 'Access denied: Doctor not assigned to this patient'}, status=403)
                    except requests.RequestException:
                        return JsonResponse({'error': 'Failed to validate doctor-patient relationship'}, status=500)

                # Proceed with update
                payload = {"Notes": notes}
                url = f"{PMRM_BASE_URL}/medical_conditions/{patient_nat_id}/{med_condition}/"
                response = requests.put(url, json=payload)

            else:
                # Add medical condition
                patient_nat_id = request.POST.get('PatientNatID')
                med_condition = request.POST.get('MedCondition')
                notes = request.POST.get('Notes', '')  # Default to empty string

                if not patient_nat_id or not med_condition:
                    return JsonResponse({"error": "Missing required fields for addition"}, status=400)

                # Role-based access validation
                if user_role == 'patient':
                    return JsonResponse({'error': 'Access denied: Patients cannot add records'}, status=403)

                if user_role == 'doctor' and patient_nat_id:
                    # Validate doctor-patient relationship
                    relationship_url = f"{PMRM_BASE_URL}/treated_by/{patient_nat_id}/{doctor_id}/"
                    try:
                        relationship_response = requests.get(relationship_url)
                        if relationship_response.status_code != 200:
                            return JsonResponse({'error': 'Access denied: Doctor not assigned to this patient'}, status=403)
                    except requests.RequestException:
                        return JsonResponse({'error': 'Failed to validate doctor-patient relationship'}, status=500)

                # Proceed with addition
                payload = {"PatientNatID": patient_nat_id, "MedCondition": med_condition, "Notes": notes}
                url = f"{PMRM_BASE_URL}/medical_conditions/"
                response = requests.post(url, json=payload)

            response.raise_for_status()
            return HttpResponseRedirect('/medical_conditions_page/')

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to process the request: {str(e)}"}, status=500)

    def delete(self, request, patient_nat_id, med_condition):
        """
        Handles DELETE requests to delete medical conditions.
        Role-based access:
        - Only admins can delete records.
        """
        user_role = request.user_role  # Extracted from middleware

        if user_role != 'admin':
            return JsonResponse({'error': 'Access denied: Only admins can delete records'}, status=403)

        try:
            url = f"{PMRM_BASE_URL}/medical_conditions/{patient_nat_id}/{med_condition}/"
            response = requests.delete(url)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to delete medical condition: {str(e)}"}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class MedicalTestView(View):
    def get(self, request):
        """
        Handles GET requests for fetching all or specific medical tests.
        """
        patient_nat_id = request.GET.get('patient_nat_id')
        test_id = request.GET.get('test_id')

        try:
            if patient_nat_id and test_id:
                # Fetch specific medical test
                url = f"{PMRM_BASE_URL}/medical_tests/{patient_nat_id}/{test_id}/"
            else:
                # Fetch all medical tests
                url = f"{PMRM_BASE_URL}/medical_tests/"

            response = requests.get(url)
            response.raise_for_status()
            return JsonResponse(response.json(), safe=False, status=response.status_code)

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to fetch medical tests: {str(e)}"}, status=500)

    def post(self, request):
        """
        Handles POST requests to add, update, or delete medical tests based on the '_method' override.
        """
        try:
            method_override = request.POST.get('_method', '').lower()

            if method_override == 'put':
                # Update medical test
                patient_nat_id = request.POST.get('patient_nat_id')
                test_id = request.POST.get('test_id')
                payload = {
                    "Test_Type": request.POST.get('Test_Type'),
                    "SubjectOfTest": request.POST.get('SubjectOfTest'),
                    "Result": request.POST.get('Result'),
                    "ImageOfScan": request.POST.get('ImageOfScan'),  # Now accepts text input
                    "Date_TimeOfUpload": request.POST.get('Date_TimeOfUpload'),
                }
                if not patient_nat_id or not test_id:
                    return JsonResponse({"error": "Missing required fields for update"}, status=400)

                url = f"{PMRM_BASE_URL}/medical_tests/{patient_nat_id}/{test_id}/"
                response = requests.put(url, json=payload)

            elif method_override == 'delete':
                # Delete medical test
                patient_nat_id = request.POST.get('patient_nat_id')
                test_id = request.POST.get('test_id')
                if not patient_nat_id or not test_id:
                    return JsonResponse({"error": "Missing required fields for deletion"}, status=400)

                url = f"{PMRM_BASE_URL}/medical_tests/{patient_nat_id}/{test_id}/"
                response = requests.delete(url)

            else:
                # Add medical test
                payload = {
                    "PatientNatID": request.POST.get('PatientNatID'),
                    "TestID": request.POST.get('TestID'),
                    "Test_Type": request.POST.get('Test_Type'),
                    "SubjectOfTest": request.POST.get('SubjectOfTest'),
                    "Result": request.POST.get('Result'),
                    "ImageOfScan": request.POST.get('ImageOfScan'),  # Now accepts text input
                    "Date_TimeOfUpload": request.POST.get('Date_TimeOfUpload'),
                }
                if not payload["PatientNatID"] or not payload["TestID"]:
                    return JsonResponse({"error": "Missing required fields for addition"}, status=400)

                url = f"{PMRM_BASE_URL}/medical_tests/"
                response = requests.post(url, json=payload)

            response.raise_for_status()
            return HttpResponseRedirect('/medical_tests_page/')

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to process the request: {str(e)}"}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class TreatedByView(View):
    def get(self, request):
        """
        Handles GET requests for fetching all or specific treated-by records.
        """
        patient_nat_id = request.GET.get('patient_nat_id')
        doctor_nat_id = request.GET.get('doctor_nat_id')

        try:
            if patient_nat_id and doctor_nat_id:
                # Fetch specific treated-by record
                url = f"{PMRM_BASE_URL}/treated_by/{patient_nat_id}/{doctor_nat_id}/"
            else:
                # Fetch all treated-by records
                url = f"{PMRM_BASE_URL}/treated_by/"

            response = requests.get(url)
            response.raise_for_status()
            return JsonResponse(response.json(), safe=False, status=response.status_code)

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to fetch treated-by records: {str(e)}"}, status=500)

    def post(self, request):
        """
        Handles POST requests to add, update, or delete treated-by relationships based on the '_method' override.
        """
        try:
            method_override = request.POST.get('_method', '').lower()

            if method_override == 'put':
                # Update treated-by relationship
                patient_nat_id = request.POST.get('patient_nat_id')
                doctor_nat_id = request.POST.get('doctor_nat_id')
                start_date = request.POST.get('start_date') 
                payload = {"start_date": start_date}
                if not patient_nat_id or not doctor_nat_id:
                    return JsonResponse({"error": "Missing required fields for update"}, status=400)

                url = f"{PMRM_BASE_URL}/treated_by/{patient_nat_id}/{doctor_nat_id}/"
                response = requests.put(url, json=payload)

            elif method_override == 'delete':
                # Delete treated-by relationship
                patient_nat_id = request.POST.get('patient_nat_id')
                doctor_nat_id = request.POST.get('doctor_nat_id')
                if not patient_nat_id or not doctor_nat_id:
                    return JsonResponse({"error": "Missing required fields for deletion"}, status=400)

                url = f"{PMRM_BASE_URL}/treated_by/{patient_nat_id}/{doctor_nat_id}/"
                response = requests.delete(url)

            else:
                # Add treated-by relationship
                payload = {
                    "PatientNatID": request.POST.get('PatientNatID'),
                    "DoctorNatID": request.POST.get('DoctorNatID'),
                    "start_date": request.POST.get('start_date'),
                }
                if not payload["PatientNatID"] or not payload["DoctorNatID"]:
                    return JsonResponse({"error": "Missing required fields for addition"}, status=400)

                url = f"{PMRM_BASE_URL}/treated_by/"
                response = requests.post(url, json=payload)

            response.raise_for_status()
            return HttpResponseRedirect('/treated_by_page/')

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to process the request: {str(e)}"}, status=500)