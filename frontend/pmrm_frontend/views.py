from django.http import JsonResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

PMRM_BASE_URL = "http://127.0.0.1:8002/api/pmrm"



def home(request):
    """
    Renders the homepage with links and forms for GET, POST, and PUT operations.
    """
    return render(request, 'home.html')

@method_decorator(csrf_exempt, name='dispatch')
class MedicalConditionView(View):
    def get(self, request):
        """
        Handles GET requests for fetching all or specific medical conditions.
        """
        patient_nat_id = request.GET.get('patient_nat_id')
        med_condition = request.GET.get('med_condition')

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
        """
        try:
            # Determine if it's an add or update request
            if 'PatientNatID' in request.POST:
                # Add medical condition
                payload = {
                    "PatientNatID": request.POST['PatientNatID'],
                    "MedCondition": request.POST['MedCondition'],
                    "Notes": request.POST.get('Notes', '')
                }
                url = f"{PMRM_BASE_URL}/medical_conditions/"
                response = requests.post(url, json=payload)
            else:
                # Update medical condition
                payload = {
                    "Notes": request.POST['notes']
                }
                patient_nat_id = request.POST['patient_nat_id']
                med_condition = request.POST['med_condition']
                url = f"{PMRM_BASE_URL}/medical_conditions/{patient_nat_id}/{med_condition}/"
                response = requests.put(url, json=payload)

            response.raise_for_status()
            return HttpResponseRedirect('/')

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to process the request: {str(e)}"}, status=500)


    def put(self, request, patient_nat_id, med_condition):
        """
        Update a specific medical condition.
        """
        try:
            data = json.loads(request.body)
            url = f"{PMRM_BASE_URL}/medical_conditions/{patient_nat_id}/{med_condition}/"
            response = requests.put(url, json=data)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to update medical condition: {str(e)}"}, status=500)

    def delete(self, request, patient_nat_id, med_condition):
        """
        Delete a specific medical condition.
        """
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
                # Fetch a specific medical test
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
        Handles POST requests to add a new medical test.
        """
        try:
            payload = {
                "PatientNatID": request.POST['PatientNatID'],
                "TestID": request.POST['TestID'],
                "Test_Type": request.POST.get('Test_Type', ''),
                "SubjectOfTest": request.POST.get('SubjectOfTest', ''),
                "Result": request.POST.get('Result', ''),
                "Date_TimeOfUpload": request.POST.get('Date_TimeOfUpload', '')
            }

            # Handle file upload if provided
            files = {"ImageOfScan": request.FILES['ImageOfScan']} if 'ImageOfScan' in request.FILES else None

            url = f"{PMRM_BASE_URL}/medical_tests/"
            response = requests.post(url, data=payload, files=files)
            response.raise_for_status()
            return HttpResponseRedirect('/')

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to add medical test: {str(e)}"}, status=500)

    def put(self, request, patient_nat_id, test_id):
        """
        Handles PUT requests to update a medical test.
        """
        try:
            data = json.loads(request.body)
            url = f"{PMRM_BASE_URL}/medical_tests/{patient_nat_id}/{test_id}/"
            response = requests.put(url, json=data)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to update medical test: {str(e)}"}, status=500)

    def delete(self, request, patient_nat_id, test_id):
        """
        Handles DELETE requests to remove a medical test.
        """
        try:
            url = f"{PMRM_BASE_URL}/medical_tests/{patient_nat_id}/{test_id}/"
            response = requests.delete(url)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to delete medical test: {str(e)}"}, status=500)


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
        Handles POST requests to add a treated-by relationship.
        """
        try:
            payload = {
                "PatientNatID": request.POST['PatientNatID'],
                "DoctorNatID": request.POST['DoctorNatID'],
                "startDate": request.POST.get('startDate', '')
            }

            url = f"{PMRM_BASE_URL}/treated_by/"
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return HttpResponseRedirect('/')

        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to add treated-by relationship: {str(e)}"}, status=500)

    def put(self, request, patient_nat_id, doctor_nat_id):
        """
        Handles PUT requests to update a treated-by relationship.
        """
        try:
            data = json.loads(request.body)
            url = f"{PMRM_BASE_URL}/treated_by/{patient_nat_id}/{doctor_nat_id}/"
            response = requests.put(url, json=data)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to update treated-by relationship: {str(e)}"}, status=500)

    def delete(self, request, patient_nat_id, doctor_nat_id):
        """
        Handles DELETE requests to remove a treated-by relationship.
        """
        try:
            url = f"{PMRM_BASE_URL}/treated_by/{patient_nat_id}/{doctor_nat_id}/"
            response = requests.delete(url)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({"error": f"Failed to delete treated-by relationship: {str(e)}"}, status=500)