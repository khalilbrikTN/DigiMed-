from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from functools import wraps
import requests
import json  # Import the json module

# Base URL for Database Management Service
DBMS_BASE_URL = "http://127.0.0.1:8000/api/dbms"

class AdminAuthorization:
    def is_admin(self, user):
        return user == "admin"

    def require_admin(self, func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            user_role = request.headers.get("Role", "user")
            if user_role != "admin":
                return JsonResponse({"error": "Unauthorized access - Admins only"}, status=403)
            return func(request, *args, **kwargs)
        return wrapper

admin_auth = AdminAuthorization()

@method_decorator(csrf_exempt, name='dispatch')
class MedicalConditionView(View):
    """
    Handles medical conditions related operations.
    """

    def post(self, request):
        try:
            data = json.loads(request.body)
            print("Received data (MedicalCondition POST):", data)  # Debugging statement
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        required_fields = ["PatientNatID", "MedCondition"]
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return JsonResponse({"error": f"Missing required fields: {', '.join(missing_fields)}"}, status=400)
        json_payload = {
            "PatientNatID": data.get("PatientNatID"),
            "MedCondition": data.get("MedCondition"),
            "Notes": data.get("Notes")
        }
        try:
            response = requests.post(f'{DBMS_BASE_URL}/medicalConditions/', json=json_payload)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (MedicalCondition POST):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (MedicalCondition POST):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def get(self, request, patient_nat_id, med_condition):
        try:
            response = requests.get(f'{DBMS_BASE_URL}/medicalConditions/{patient_nat_id}/{med_condition}/')
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (MedicalCondition GET):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (MedicalCondition GET):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def put(self, request, patient_nat_id, med_condition):
        try:
            data = json.loads(request.body)
            print("Received data (MedicalCondition PUT):", data)  # Debugging statement
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        json_payload = {
            "Notes": data.get("Notes")
        }
        try:
            response = requests.put(f'{DBMS_BASE_URL}/medicalConditions/{patient_nat_id}/{med_condition}/', json=json_payload)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (MedicalCondition PUT):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (MedicalCondition PUT):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    @method_decorator(admin_auth.require_admin)
    def delete(self, request, patient_nat_id, med_condition):
        try:
            response = requests.delete(f'{DBMS_BASE_URL}/medicalConditions/{patient_nat_id}/{med_condition}/')
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (MedicalCondition DELETE):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (MedicalCondition DELETE):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class MedicalTestView(View):
    """
    Handles medical tests related operations.
    """

    def post(self, request):
        try:
            data = json.loads(request.body)
            print("Received data (MedicalTest POST):", data)  # Debugging statement
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        required_fields = ["PatientNatID", "TestID", "Test_Type", "SubjectOfTest", "Result", "Date_TimeOfUpload"]
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return JsonResponse({"error": f"Missing required fields: {', '.join(missing_fields)}"}, status=400)
        json_payload = {
            "PatientNatID": data.get("PatientNatID"),
            "TestID": data.get("TestID"),
            "Test_Type": data.get("Test_Type"),
            "SubjectOfTest": data.get("SubjectOfTest"),
            "Result": data.get("Result"),
            "ImageOfScan": data.get("ImageOfScan"),
            "Date_TimeOfUpload": data.get("Date_TimeOfUpload")
        }
        try:
            response = requests.post(f'{DBMS_BASE_URL}/medicalTests/', json=json_payload)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (MedicalTest POST):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (MedicalTest POST):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def get(self, request, patient_nat_id, test_id):
        try:
            response = requests.get(f'{DBMS_BASE_URL}/medicalTests/{patient_nat_id}/{test_id}/')
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (MedicalTest GET):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (MedicalTest GET):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def put(self, request, patient_nat_id, test_id):
        try:
            data = json.loads(request.body)
            print("Received data (MedicalTest PUT):", data)  # Debugging statement
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        json_payload = {
            "Test_Type": data.get("Test_Type"),
            "SubjectOfTest": data.get("SubjectOfTest"),
            "Result": data.get("Result"),
            "ImageOfScan": data.get("ImageOfScan"),
            "Date_TimeOfUpload": data.get("Date_TimeOfUpload")
        }
        try:
            response = requests.put(f'{DBMS_BASE_URL}/medicalTests/{patient_nat_id}/{test_id}/', json=json_payload)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (MedicalTest PUT):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (MedicalTest PUT):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    @method_decorator(admin_auth.require_admin)
    def delete(self, request, patient_nat_id, test_id):
        try:
            response = requests.delete(f'{DBMS_BASE_URL}/medicalTests/{patient_nat_id}/{test_id}/')
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (MedicalTest DELETE):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (MedicalTest DELETE):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class TreatedByView(View):
    """
    Handles doctor-patient treatment assignments.
    """

    def post(self, request):
        try:
            data = json.loads(request.body)
            print("Received data (TreatedBy POST):", data)  # Debugging statement
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        required_fields = ["PatientNatID", "DoctorNatID", "startDate"]
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return JsonResponse({"error": f"Missing required fields: {', '.join(missing_fields)}"}, status=400)
        json_payload = {
            "PatientNatID": data.get("PatientNatID"),
            "DoctorNatID": data.get("DoctorNatID"),
            "startDate": data.get("startDate")
        }
        try:
            response = requests.post(f'{DBMS_BASE_URL}/treatedBy/', json=json_payload)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (TreatedBy POST):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (TreatedBy POST):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def get(self, request, patient_nat_id, doctor_nat_id):
        try:
            response = requests.get(f'{DBMS_BASE_URL}/treatedBy/{patient_nat_id}/{doctor_nat_id}/')
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (TreatedBy GET):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (TreatedBy GET):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def put(self, request, patient_nat_id, doctor_nat_id):
        try:
            data = json.loads(request.body)
            print("Received data (TreatedBy PUT):", data)  # Debugging statement
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        json_payload = {
            "startDate": data.get("startDate")
        }
        try:
            response = requests.put(f'{DBMS_BASE_URL}/treatedBy/{patient_nat_id}/{doctor_nat_id}/', json=json_payload)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (TreatedBy PUT):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (TreatedBy PUT):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    @method_decorator(admin_auth.require_admin)
    def delete(self, request, patient_nat_id, doctor_nat_id):
        try:
            response = requests.delete(f'{DBMS_BASE_URL}/treatedBy/{patient_nat_id}/{doctor_nat_id}/')
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (TreatedBy DELETE):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (TreatedBy DELETE):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)