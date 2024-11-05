# Import Flask and jsonify for API Gateway communication
from flask import Flask, request, jsonify
# Import gRPC for communication with services
import grpc
# Import the generated gRPC classes
import PMRM_Service_pb2
import PMRM_Service_pb2_grpc
# Used for creating decorated functions
from functools import wraps

# Initializing the Flask app
app = Flask(__name__)

class PatientMedicalRecordService:

    # Address is database_management_service:50051
    #Will be changed according to the service name and port in the docker-compose file
    grpc_address = 'database_management_service:50051'

    def __init__(self):
        # Creating the gRPC channel for communication with the database management service
        self.channel = grpc.insecure_channel(self.grpc_address)  
        # This stub allows us to call the gRPC methods on the server
        self.stub = PMRM_Service_pb2_grpc.PMRMServiceStub(self.channel)

    # Helper function to check if the user is an admin
    # Should be changed to how the user is actully authenticated 
    def is_admin(self, user):
        return user == "admin"

    # Decorator function to restrict access to admin users
    def require_admin(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user_role = request.headers.get("Role", "user")
            if user_role != "admin":
                return jsonify({"error": "Unauthorized access - Admins only"}), 403
            return f(*args, **kwargs)
        return wrapper

    # MedicalConditions: Create record
    def create_medical_condition(self):
        data = request.json
        grpc_request = PMRM_Service_pb2.CreateMedicalConditionRequest(
            table_name="MedicalConditions",
            PatientNatID=data.get("PatientNatID"),
            MedCondition=data.get("MedCondition"),
            Notes=data.get("Notes")
        )
        try:
            grpc_response = self.stub.CreateMedicalCondition(grpc_request)
            return jsonify({"status": grpc_response.status}), 201
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to create medical condition: {e.details()}", "code": e.code().name}), 500

    # MedicalConditions: Retrieve record
    def retrieve_medical_condition(self, patient_nat_id, med_condition):
        grpc_request = PMRM_Service_pb2.RetrieveMedicalConditionRequest(
            table_name="MedicalConditions",
            PatientNatID=patient_nat_id,
            MedCondition=med_condition
        )
        try:
            grpc_response = self.stub.RetrieveMedicalCondition(grpc_request)
            return jsonify({
                "status": grpc_response.status,
                "PatientNatID": grpc_response.PatientNatID,
                "MedCondition": grpc_response.MedCondition,
                "Notes": grpc_response.Notes
            })
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to retrieve medical condition: {e.details()}", "code": e.code().name}), 500

    # MedicalTests: Create record
    def create_medical_test(self):
        data = request.json
        grpc_request = PMRM_Service_pb2.CreateMedicalTestRequest(
            table_name="MedicalTests",
            PatientNatID=data.get("PatientNatID"),
            TestID=data.get("TestID"),
            Test_Type=data.get("Test_Type", ""),
            SubjectOfTest=data.get("SubjectOfTest", ""),
            Result=data.get("Result", ""),
            ImageOfScan=data.get("ImageOfScan", ""),
            Date_TimeOfUpload=data.get("Date_TimeOfUpload", "")
        )
        try:
            grpc_response = self.stub.CreateMedicalTest(grpc_request)
            return jsonify({"status": grpc_response.status}), 201
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to create medical test: {e.details()}", "code": e.code().name}), 500

    # TreatedBy: Create record
    def create_treated_by(self):
        data = request.json
        grpc_request = PMRM_Service_pb2.CreateTreatedByRequest(
            table_name="TreatedBy",
            PatientNatID=data.get("PatientNatID"),
            DoctorNatID=data.get("DoctorNatID"),
            startDate=data.get("startDate", "")
        )
        try:
            grpc_response = self.stub.CreateTreatedBy(grpc_request)
            return jsonify({"status": grpc_response.status}), 201
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to create treated-by record: {e.details()}", "code": e.code().name}), 500

    # Example retrieve method for TreatedBy
    def retrieve_treated_by(self, patient_nat_id, doctor_nat_id):
        grpc_request = PMRM_Service_pb2.RetrieveTreatedByRequest(
            table_name="TreatedBy",
            PatientNatID=patient_nat_id,
            DoctorNatID=doctor_nat_id
        )
        try:
            grpc_response = self.stub.RetrieveTreatedBy(grpc_request)
            return jsonify({
                "status": grpc_response.status,
                "PatientNatID": grpc_response.PatientNatID,
                "DoctorNatID": grpc_response.DoctorNatID,
                "startDate": grpc_response.startDate
            })
        except grpc.RpcError as( e):
            return jsonify({"error": f"Failed to retrieve treated-by record: {e.details()}", "code": e.code().name}), 500


# Instance of the service class
pmrm_service = PatientMedicalRecordService()

# Flask route bindings to the instance methods of the class for each table and operation
app.add_url_rule('/medical_conditions', view_func=pmrm_service.create_medical_condition, methods=['POST'])
app.add_url_rule('/medical_conditions/<string:patient_nat_id>/<string:med_condition>', view_func=pmrm_service.retrieve_medical_condition, methods=['GET'])
app.add_url_rule('/medical_tests', view_func=pmrm_service.create_medical_test, methods=['POST'])
app.add_url_rule('/treated_by', view_func=pmrm_service.create_treated_by, methods=['POST'])
app.add_url_rule('/treated_by/<string:patient_nat_id>/<string:doctor_nat_id>', view_func=pmrm_service.retrieve_treated_by, methods=['GET'])

# Allows the app to receive requests from the API Gateway
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
