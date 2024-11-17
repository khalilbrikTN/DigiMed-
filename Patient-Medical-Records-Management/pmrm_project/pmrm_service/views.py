from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from functools import wraps
import requests

# Base URL Database Management Service
DB_SERVICE_URL = 'http://database_management_service/api'


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


class MedicalConditions:
    def create_medical_condition(self, request):
        data = request.POST
        grpc_request = {
            "table_name": "MedicalConditions",
            "PatientNatID": data.get("PatientNatID"),
            "MedCondition": data.get("MedCondition"),
            "Notes": data.get("Notes")
        }
        response = requests.post(f'{DB_SERVICE_URL}/medicalConditions', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)

    def retrieve_medical_condition(self, request, patient_nat_id, med_condition):
        grpc_request = {
            "table_name": "MedicalConditions",
            "PatientNatID": patient_nat_id,
            "MedCondition": med_condition
        }
        response = requests.post(f'{DB_SERVICE_URL}/medicalConditions/retrieve', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)

    def edit_medical_condition(self, request, patient_nat_id, med_condition):
        data = request.POST
        grpc_request = {
            "table_name": "MedicalConditions",
            "PatientNatID": patient_nat_id,
            "MedCondition": med_condition,
            "Notes": data.get("Notes")
        }
        response = requests.put(f'{DB_SERVICE_URL}/medicalConditions', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)

    @admin_auth.require_admin
    def delete_medical_condition(self, request, patient_nat_id, med_condition):
        grpc_request = {
            "table_name": "MedicalConditions",
            "PatientNatID": patient_nat_id,
            "MedCondition": med_condition
        }
        response = requests.delete(f'{DB_SERVICE_URL}/medicalConditions', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)


class MedicalTests:
    def create_medical_test(self, request):
        data = request.POST
        grpc_request = {
            "table_name": "MedicalTests",
            "PatientNatID": data.get("PatientNatID"),
            "TestID": data.get("TestID"),
            "Test_Type": data.get("Test_Type"),
            "SubjectOfTest": data.get("SubjectOfTest"),
            "Result": data.get("Result"),
            "ImageOfScan": data.get("ImageOfScan"),
            "Date_TimeOfUpload": data.get("Date_TimeOfUpload")
        }
        response = requests.post(f'{DB_SERVICE_URL}/medicalTests', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)

    def retrieve_medical_test(self, request, patient_nat_id, test_id):
        grpc_request = {
            "table_name": "MedicalTests",
            "PatientNatID": patient_nat_id,
            "TestID": test_id
        }
        response = requests.post(f'{DB_SERVICE_URL}/medicalTests/retrieve', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)

    def edit_medical_test(self, request, patient_nat_id, test_id):
        data = request.POST
        grpc_request = {
            "table_name": "MedicalTests",
            "PatientNatID": patient_nat_id,
            "TestID": test_id,
            "Test_Type": data.get("Test_Type"),
            "SubjectOfTest": data.get("SubjectOfTest"),
            "Result": data.get("Result"),
            "ImageOfScan": data.get("ImageOfScan"),
            "Date_TimeOfUpload": data.get("Date_TimeOfUpload")
        }
        response = requests.put(f'{DB_SERVICE_URL}/medicalTests', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)

    @admin_auth.require_admin
    def delete_medical_test(self, request, patient_nat_id, test_id):
        grpc_request = {
            "table_name": "MedicalTests",
            "PatientNatID": patient_nat_id,
            "TestID": test_id
        }
        response = requests.delete(f'{DB_SERVICE_URL}/medicalTests', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)


class TreatedBy:
    def create_treated_by(self, request):
        data = request.POST
        grpc_request = {
            "table_name": "TreatedBy",
            "PatientNatID": data.get("PatientNatID"),
            "DoctorNatID": data.get("DoctorNatID"),
            "startDate": data.get("startDate")
        }
        response = requests.post(f'{DB_SERVICE_URL}/treatedBy', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)

    def retrieve_treated_by(self, request, patient_nat_id, doctor_nat_id):
        grpc_request = {
            "table_name": "TreatedBy",
            "PatientNatID": patient_nat_id,
            "DoctorNatID": doctor_nat_id
        }
        response = requests.post(f'{DB_SERVICE_URL}/treatedBy/retrieve', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)

    def edit_treated_by(self, request, patient_nat_id, doctor_nat_id):
        data = request.POST
        grpc_request = {
            "table_name": "TreatedBy",
            "PatientNatID": patient_nat_id,
            "DoctorNatID": doctor_nat_id,
            "startDate": data.get("startDate")
        }
        response = requests.put(f'{DB_SERVICE_URL}/treatedBy', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)

    @admin_auth.require_admin
    def delete_treated_by(self, request, patient_nat_id, doctor_nat_id):
        grpc_request = {
            "table_name": "TreatedBy",
            "PatientNatID": patient_nat_id,
            "DoctorNatID": doctor_nat_id
        }
        response = requests.delete(f'{DB_SERVICE_URL}/treatedBy', json=grpc_request)
        return JsonResponse(response.json(), status=response.status_code)


class PatientMedicalRecordService:
    def __init__(self):
        self.medical_conditions = MedicalConditions()
        self.medical_tests = MedicalTests()
        self.treated_by = TreatedBy()

# Initialize service
pmrm_service = PatientMedicalRecordService()
