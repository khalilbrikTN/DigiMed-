from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from functools import wraps
import requests
import json  # Import the json module

# Base URL for Database Management Service
DBMS_BASE_URL = "http://127.0.0.1:8001/api/dbms"

class AdminAuthorization:
    def is_admin(self, user):
        return user == "admin"

    def require_admin(self, func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            user_role = request.headers.get("Role", "admin")
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
            "Notes": data.get("Notes", "")  # Default to empty string if Notes is missing
        }
        try:
            dbms_url = f'{DBMS_BASE_URL}/medicalConditions/'
            print(f"Forwarding POST to DBMS: {dbms_url}, Payload: {json_payload}")  # Debugging

            response = requests.post(dbms_url, json=json_payload)
            print(f"DBMS Response Status: {response.status_code}, Response: {response.text}")  # Debugging

            if response.status_code == 201:
                return JsonResponse(response.json(), status=201)

            # For other statuses, parse and return the response JSON
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"RequestException (MedicalCondition POST): {e}")  # Log error
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print(f"ValueError (MedicalCondition POST): {e}")  # Log JSON parsing error
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def get(self, request, patient_nat_id, med_condition):
        try:
            dbms_url = f'{DBMS_BASE_URL}/medicalConditions/{patient_nat_id}/{med_condition}/'
            print(f"Forwarding GET to DBMS: {dbms_url}")  # Debugging

            response = requests.get(dbms_url)
            print(f"DBMS Response Status: {response.status_code}, Response: {response.text}")  # Debugging

            if response.status_code == 200:
                return JsonResponse(response.json(), status=200)

            # Handle 404 Not Found explicitly
            if response.status_code == 404:
                return JsonResponse({"error": "Record not found"}, status=404)

            # For other statuses, parse and return the response JSON
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"RequestException (MedicalCondition GET): {e}")  # Log error
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print(f"ValueError (MedicalCondition GET): {e}")  # Log JSON parsing error
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def put(self, request, patient_nat_id, med_condition):
        try:
            data = json.loads(request.body)
            print("Received data (MedicalCondition PUT):", data)  # Debugging

            json_payload = {"Notes": data.get("Notes")}
            dbms_url = f'{DBMS_BASE_URL}/medicalConditions/{patient_nat_id}/{med_condition}/'
            print(f"Forwarding PUT to DBMS: {dbms_url}, Payload: {json_payload}")  # Debugging

            response = requests.put(dbms_url, json=json_payload)
            print(f"DBMS Response Status: {response.status_code}, Response: {response.text}")  # Debugging

            if response.status_code == 204:
                return JsonResponse({"message": "Updated successfully"}, status=204)

            # For other statuses, parse and return the response JSON
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"RequestException (MedicalCondition PUT): {e}")  # Log error
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print(f"ValueError (MedicalCondition PUT): {e}")  # Log JSON parsing error
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    @method_decorator(admin_auth.require_admin)
    def delete(self, request, patient_nat_id, med_condition):
        try:
            dbms_url = f'{DBMS_BASE_URL}/medicalConditions/{patient_nat_id}/{med_condition}/'
            print(f"Forwarding DELETE to DBMS: {dbms_url}")  # Debugging

            response = requests.delete(dbms_url)
            print(f"DBMS Response Status: {response.status_code}")  # Log status

            if response.status_code == 204:
                return JsonResponse({"message": "Deleted successfully"}, status=204)

            # For other statuses, parse and return the response JSON
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"RequestException (MedicalCondition DELETE): {e}")  # Log error
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print(f"ValueError (MedicalCondition DELETE): {e}")  # Log JSON parsing error
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
            dbms_url = f'{DBMS_BASE_URL}/medicalTests/'
            print(f"Forwarding POST to DBMS: {dbms_url}, Payload: {json_payload}")  # Debugging

            response = requests.post(dbms_url, json=json_payload)
            print(f"DBMS Response Status: {response.status_code}, Response: {response.text}")  # Debugging

            if response.status_code == 201:
                return JsonResponse(response.json(), status=201)

            # For other statuses, parse and return the response JSON
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"RequestException (MedicalTest POST): {e}")  # Log error
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print(f"ValueError (MedicalTest POST): {e}")  # Log JSON parsing error
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def get(self, request, patient_nat_id, test_id):
        try:
            dbms_url = f'{DBMS_BASE_URL}/medicalTests/{patient_nat_id}/{test_id}/'
            print(f"Forwarding GET to DBMS: {dbms_url}")  # Debugging

            response = requests.get(dbms_url)
            print(f"DBMS Response Status: {response.status_code}, Response: {response.text}")  # Debugging

            if response.status_code == 200:
                return JsonResponse(response.json(), status=200)

            # Handle 404 Not Found explicitly
            if response.status_code == 404:
                return JsonResponse({"error": "Record not found"}, status=404)

            # For other statuses, parse and return the response JSON
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"RequestException (MedicalTest GET): {e}")  # Log error
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print(f"ValueError (MedicalTest GET): {e}")  # Log JSON parsing error
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def put(self, request, patient_nat_id, test_id):
        try:
            data = json.loads(request.body)
            print("Received data (MedicalTest PUT):", data)  # Debugging statement

            json_payload = {
                "Test_Type": data.get("Test_Type"),
                "SubjectOfTest": data.get("SubjectOfTest"),
                "Result": data.get("Result"),
                "ImageOfScan": data.get("ImageOfScan"),
                "Date_TimeOfUpload": data.get("Date_TimeOfUpload")
            }
            dbms_url = f'{DBMS_BASE_URL}/medicalTests/{patient_nat_id}/{test_id}/'
            print(f"Forwarding PUT to DBMS: {dbms_url}, Payload: {json_payload}")  # Debugging

            response = requests.put(dbms_url, json=json_payload)
            print(f"DBMS Response Status: {response.status_code}, Response: {response.text}")  # Debugging

            if response.status_code == 204:
                return JsonResponse({"message": "Updated successfully"}, status=204)

            # For other statuses, parse and return the response JSON
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"RequestException (MedicalTest PUT): {e}")  # Log error
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print(f"ValueError (MedicalTest PUT): {e}")  # Log JSON parsing error
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    @method_decorator(admin_auth.require_admin)
    def delete(self, request, patient_nat_id, test_id):
        try:
            dbms_url = f'{DBMS_BASE_URL}/medicalTests/{patient_nat_id}/{test_id}/'
            print(f"Forwarding DELETE to DBMS: {dbms_url}")  # Debugging

            response = requests.delete(dbms_url)
            print(f"DBMS Response Status: {response.status_code}")  # Log status

            if response.status_code == 204:
                return JsonResponse({"message": "Deleted successfully"}, status=204)

            # For other statuses, parse and return the response JSON
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"RequestException (MedicalTest DELETE): {e}")  # Log error
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print(f"ValueError (MedicalTest DELETE): {e}")  # Log JSON parsing error
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

        required_fields = ["PatientNatID", "DoctorNatID", "start_date"]
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return JsonResponse({"error": f"Missing required fields: {', '.join(missing_fields)}"}, status=400)
        json_payload = {
            "PatientNatID": data.get("PatientNatID"),
            "DoctorNatID": data.get("DoctorNatID"),
            "start_date": data.get("start_date")
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
            "start_date": data.get("start_date")
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
            dbms_url = f'{DBMS_BASE_URL}/treatedBy/{patient_nat_id}/{doctor_nat_id}/'
            print(f"Forwarding DELETE to DBMS: {dbms_url}")  # Debugging
            response = requests.delete(dbms_url)
            print(f"DBMS Response Status: {response.status_code}")  # Log status

            # Handle 204 No Content explicitly
            if response.status_code == 204:
                return JsonResponse({"message": "Deleted successfully"}, status=204)

            # For other statuses, parse and return the response JSON
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print(f"RequestException (TreatedBy DELETE): {e}")  # Log error
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print(f"ValueError (TreatedBy DELETE): {e}")  # Log JSON parsing error
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)