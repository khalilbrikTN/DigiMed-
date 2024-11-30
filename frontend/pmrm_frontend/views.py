# pmrm_frontend/views.py

from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests

PMRM_BASE_URL = "http://127.0.0.1:8000/api/pmrm"

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
    Renders the Medical Conditions page and passes the role and IDs.
    """
    role = request.GET.get('role')
    nat_id = request.GET.get('nat_id', None)
    doctor_id = request.GET.get('doctor_id', None)

    # Debugging: Print received parameters
    print(f"View - Role: {role}, NatID: {nat_id}, DoctorID: {doctor_id}")

    # Validate role and IDs
    if not role:
        return render(request, 'error.html', {'message': 'Role is required to access this page.'})

    # Pass the parameters to the template
    context = {
        'role': role,
        'nat_id': nat_id if role == 'patient' else None,
        'doctor_id': doctor_id if role == 'doctor' else None,
    }
    return render(request, 'medical_conditions.html', context)

@method_decorator(csrf_exempt, name='dispatch')
class MedicalConditionView(View):
    def get(self, request, patient_nat_id=None, med_condition=None):
        # No role checks here
        try:
            if patient_nat_id and med_condition:
                # Fetch specific medical condition
                url = f"http://127.0.0.1:8000/api/pmrm/medical_conditions/{patient_nat_id}/{med_condition}/"
            else:
                # Fetch all medical conditions
                url = "http://127.0.0.1:8000/api/pmrm/medical_conditions/"

            response = requests.get(url)
            response.raise_for_status()
            return JsonResponse(response.json(), safe=False, status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to fetch medical conditions: {str(e)}"}, status=500)

    def post(self, request):
        """
        Handles POST requests to add, update, or delete medical conditions based on the '_method' override.
        """
        role = request.POST.get('role')
        nat_id = request.POST.get('nat_id', None)
        doctor_id = request.POST.get('doctor_id', None)


        try:
            # Handle method override
            method_override = request.POST.get('_method', '').lower()
            
            if method_override == 'put':
                return self.put(request)
            elif method_override == 'delete':
                return self.delete(request)

            # Add medical condition (default POST behavior)
            payload = {
                "PatientNatID": request.POST.get('PatientNatID'),
                "MedCondition": request.POST.get('MedCondition'),
                "Notes": request.POST.get('Notes', '')  # Safely get 'Notes', default to empty string
            }
            if not payload["PatientNatID"] or not payload["MedCondition"]:
                return JsonResponse({"error": "Missing required fields for addition"}, status=400)

            url = f"{PMRM_BASE_URL}/medical_conditions/"
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to process the request: {str(e)}"}, status=500)

    def put(self, request):
        """
        Update a specific medical condition.
        """
        role = request.POST.get('role')
        nat_id = request.POST.get('nat_id', None)
        doctor_id = request.POST.get('doctor_id', None)

        # Validate role and IDs
    

        try:
            patient_nat_id = request.POST.get('patient_nat_id')
            med_condition = request.POST.get('med_condition')
            notes = request.POST.get('notes', '')

            if not patient_nat_id or not med_condition:
                return JsonResponse({"error": "Missing required fields for update"}, status=400)

            payload = {"Notes": notes}
            url = f"{PMRM_BASE_URL}/medical_conditions/{patient_nat_id}/{med_condition}/"
            response = requests.put(url, json=payload)
            response.raise_for_status()
            return JsonResponse({"message": "Updated successfully"}, status=response.status_code)

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to update medical condition: {str(e)}"}, status=500)

    def delete(self, request):
        """
        Delete a specific medical condition.
        """
        role = request.POST.get('role')
        nat_id = request.POST.get('nat_id', None)
        doctor_id = request.POST.get('doctor_id', None)

        # Validate role and IDs
    
        try:
            patient_nat_id = request.POST.get('patient_nat_id')
            med_condition = request.POST.get('med_condition')

            if not patient_nat_id or not med_condition:
                return JsonResponse({"error": "Missing required fields for deletion"}, status=400)

            url = f"{PMRM_BASE_URL}/medical_conditions/{patient_nat_id}/{med_condition}/"
            response = requests.delete(url)
            response.raise_for_status()
            return JsonResponse({"message": "Deleted successfully"}, status=response.status_code)

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to delete medical condition: {str(e)}"}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
class MedicalTestView(View):
    def get(self, request):
        """
        Handles GET requests for fetching all or specific medical conditions.
        """
        role = request.GET.get('role')
        nat_id = request.GET.get('nat_id', None)
        doctor_id = request.GET.get('doctor_id', None)


        # Fetch specific or all medical conditions
        patient_nat_id = request.GET.get('patient_nat_id')
        med_condition = request.GET.get('med_condition')

        try:
            if patient_nat_id and med_condition:
                # Fetch specific medical condition
                url = f"{PMRM_BASE_URL}/medical_conditions/{patient_nat_id}/{med_condition}/"
            else:
                # Fetch all medical conditions
                url = f"{PMRM_BASE_URL}/medical_conditions/{patient_nat_id}/{med_condition}/"

            response = requests.get(url)
            response.raise_for_status()
            return JsonResponse(response.json(), safe=False, status=response.status_code)

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to fetch medical conditions: {str(e)}"}, status=500)
        
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