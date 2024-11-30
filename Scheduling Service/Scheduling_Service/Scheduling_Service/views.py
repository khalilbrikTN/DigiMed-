from django.http import HttpResponse
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
            user_role = request.headers.get("Role", "user")
            if user_role != "admin":
                return JsonResponse({"error": "Unauthorized access - Admins only"}, status=403)
            return func(request, *args, **kwargs)
        return wrapper

admin_auth = AdminAuthorization()

@method_decorator(csrf_exempt, name='dispatch')
class SchedulingView(View):
    """
    Handles Appointment Scheduling operations.
    """

    def post(self, request):
        try:
            data = json.loads(request.body)
            print("Received data (Appointments POST):", data)  # Debugging statement
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        required_fields = ["doctor", "patient", "app_id"]
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return JsonResponse({"error": f"Missing required fields: {', '.join(missing_fields)}"}, status=400)
        json_payload = {
            "doctor": data.get("doctor"),
            "patient": data.get("patient"),
            "app_date_time": data.get("app_date_time"),
            "app_id": data.get("app_id")
        }
        try:
            response = requests.post(f'{DBMS_BASE_URL}/Appointments/', json=json_payload)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (Appointments POST):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (Appointments POST):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def get(self, request, patient, doctor, app_id):
        try:
            response = requests.get(f'{DBMS_BASE_URL}/Appointments/{patient}/{doctor}/{app_id}/')
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (Appointments GET):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (Scheduling GET):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    def put(self, request, patient, doctor, app_id):
        try:
            data = json.loads(request.body)
            print("Received data (Appointments PUT):", data)  # Debugging statement
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        json_payload = {
            "app_date_time": data.get("app_date_time"),
        }
        try:
            response = requests.put(f'{DBMS_BASE_URL}/Appointments/{patient}/{doctor}/{app_id}/', json=json_payload)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (Appointments PUT):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (Appointments PUT):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)

    @method_decorator(admin_auth.require_admin)
    def delete(self, request, patient, doctor, app_id):
        try:
            response = requests.delete(f'{DBMS_BASE_URL}/Appointments/{patient}/{doctor}/{app_id}/')
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.exceptions.RequestException as e:
            print("RequestException (Appointments DELETE):", e)
            return JsonResponse({"error": "Failed to connect to the database service"}, status=500)
        except ValueError as e:
            print("ValueError (Appointments DELETE):", e)
            return JsonResponse({"error": "Invalid response from the database service"}, status=500)


