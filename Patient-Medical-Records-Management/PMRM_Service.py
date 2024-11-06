# Import Flask and jsonify for API Gateway communication
from flask import Flask, request, jsonify
import grpc
import PMRM_Service_pb2
import PMRM_Service_pb2_grpc
from functools import wraps

# Initializing the Flask app
app = Flask(__name__)

# AdminAuthorization class containing common admin functions
class AdminAuthorization:
    def is_admin(self, user):
        return user == "admin"

    def require_admin(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user_role = request.headers.get("Role", "user")
            if user_role != "admin":
                return jsonify({"error": "Unauthorized access - Admins only"}), 403
            return f(*args, **kwargs)
        return wrapper

# MedicalConditions class handling MedicalConditions-specific operations
class MedicalConditions(AdminAuthorization):
    def __init__(self, stub):
        self.stub = stub

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

    #need to implement isMedCod
    def retrieve_medical_condition(self, patient_nat_id, med_condition, isMedCod):
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
    #need to implement isMedCod
    def edit_medical_condition(self, patient_nat_id, med_condition, isMedCod):
        data = request.json
        grpc_request = PMRM_Service_pb2.UpdateMedicalConditionRequest(
            table_name="MedicalConditions",
            PatientNatID=patient_nat_id,
            MedCondition=med_condition,
            Notes=data.get("Notes", "")
        )
        try:
            grpc_response = self.stub.UpdateMedicalCondition(grpc_request)
            return jsonify({"status": grpc_response.status}), 200
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to update medical condition: {e.details()}", "code": e.code().name}), 500
    #need to implement isMedCod
    @AdminAuthorization.require_admin
    def delete_medical_condition(self, patient_nat_id, med_condition, isMedCod):
        grpc_request = PMRM_Service_pb2.DeleteMedicalConditionRequest(
            table_name="MedicalConditions",
            PatientNatID=patient_nat_id,
            MedCondition=med_condition
        )
        try:
            grpc_response = self.stub.DeleteMedicalCondition(grpc_request)
            return jsonify({"status": grpc_response.status}), 200
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to delete medical condition: {e.details()}", "code": e.code().name}), 500

# MedicalTests class handling MedicalTests-specific operations
class MedicalTests(AdminAuthorization):
    def __init__(self, stub):
        self.stub = stub

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

        #need to implement test
    def retrieve_medical_test(self, patient_nat_id, test_id, isTest):
        grpc_request = PMRM_Service_pb2.RetrieveMedicalTestRequest(
            table_name="MedicalTests",
            PatientNatID=patient_nat_id,
            TestID=test_id
        )
        try:
            grpc_response = self.stub.RetrieveMedicalTest(grpc_request)
            return jsonify({
                "status": grpc_response.status,
                "PatientNatID": grpc_response.PatientNatID,
                "TestID": grpc_response.TestID,
                "Test_Type": grpc_response.Test_Type,
                "SubjectOfTest": grpc_response.SubjectOfTest,
                "Result": grpc_response.Result,
                "ImageOfScan": grpc_response.ImageOfScan,
                "Date_TimeOfUpload": grpc_response.Date_TimeOfUpload
            })
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to retrieve medical test: {e.details()}", "code": e.code().name}), 500

        #need to implement test
    def edit_medical_test(self, patient_nat_id, test_id, isTest):
        data = request.json
        grpc_request = PMRM_Service_pb2.UpdateMedicalTestRequest(
            table_name="MedicalTests",
            PatientNatID=patient_nat_id,
            TestID=test_id,
            Test_Type=data.get("Test_Type", ""),
            SubjectOfTest=data.get("SubjectOfTest", ""),
            Result=data.get("Result", ""),
            ImageOfScan=data.get("ImageOfScan", ""),
            Date_TimeOfUpload=data.get("Date_TimeOfUpload", "")
        )
        try:
            grpc_response = self.stub.UpdateMedicalTest(grpc_request)
            return jsonify({"status": grpc_response.status}), 200
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to update medical test: {e.details()}", "code": e.code().name}), 500

    @AdminAuthorization.require_admin
    def delete_medical_test(self, patient_nat_id, test_id, isTest):
        grpc_request = PMRM_Service_pb2.DeleteMedicalTestRequest(
            table_name="MedicalTests",
            PatientNatID=patient_nat_id,
            TestID=test_id
        )
        try:
            grpc_response = self.stub.DeleteMedicalTest(grpc_request)
            return jsonify({"status": grpc_response.status}), 200
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to delete medical test: {e.details()}", "code": e.code().name}), 500

# TreatedBy class handling TreatedBy-specific operations
class TreatedBy(AdminAuthorization):
    def __init__(self, stub):
        self.stub = stub

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
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to retrieve treated-by record: {e.details()}", "code": e.code().name}), 500

    #maybe we need another parameter like hisotry id
    def edit_treated_by(self, patient_nat_id, doctor_nat_id):
        data = request.json
        grpc_request = PMRM_Service_pb2.UpdateTreatedByRequest(
            table_name="TreatedBy",
            PatientNatID=patient_nat_id,
            DoctorNatID=doctor_nat_id,
            startDate=data.get("startDate", "")
        )
        try:
            grpc_response = self.stub.UpdateTreatedBy(grpc_request)
            return jsonify({"status": grpc_response.status}), 200
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to update treated-by record: {e.details()}", "code": e.code().name}), 500

    @AdminAuthorization.require_admin
    def delete_treated_by(self, patient_nat_id, doctor_nat_id):
        grpc_request = PMRM_Service_pb2.DeleteTreatedByRequest(
            table_name="TreatedBy",
            PatientNatID=patient_nat_id,
            DoctorNatID=doctor_nat_id
        )
        try:
            grpc_response = self.stub.DeleteTreatedBy(grpc_request)
            return jsonify({"status": grpc_response.status}), 200
        except grpc.RpcError as e:
            return jsonify({"error": f"Failed to delete treated-by record: {e.details()}", "code": e.code().name}), 500

# Main PatientMedicalRecordService class
class PatientMedicalRecordService:
    def __init__(self):
        channel = grpc.insecure_channel('database_management_service:50051')
        stub = PMRM_Service_pb2_grpc.PMRMServiceStub(channel)
        
        self.medical_conditions = MedicalConditions(stub)
        self.medical_tests = MedicalTests(stub)
        self.treated_by = TreatedBy(stub)

# Instance of the main service class
pmrm_service = PatientMedicalRecordService()

# Route bindings for MedicalConditions
app.add_url_rule('/medical_conditions', view_func=pmrm_service.medical_conditions.create_medical_condition, methods=['POST'])
app.add_url_rule('/medical_conditions/<string:patient_nat_id>/<string:med_condition>', view_func=pmrm_service.medical_conditions.retrieve_medical_condition, methods=['GET'])
app.add_url_rule('/medical_conditions/<string:patient_nat_id>/<string:med_condition>', view_func=pmrm_service.medical_conditions.edit_medical_condition, methods=['PUT'])
app.add_url_rule('/medical_conditions/<string:patient_nat_id>/<string:med_condition>', view_func=pmrm_service.medical_conditions.delete_medical_condition, methods=['DELETE'])

# Route bindings for MedicalTests
app.add_url_rule('/medical_tests', view_func=pmrm_service.medical_tests.create_medical_test, methods=['POST'])
app.add_url_rule('/medical_tests/<string:patient_nat_id>/<int:test_id>', view_func=pmrm_service.medical_tests.retrieve_medical_test, methods=['GET'])
app.add_url_rule('/medical_tests/<string:patient_nat_id>/<int:test_id>', view_func=pmrm_service.medical_tests.edit_medical_test, methods=['PUT'])
app.add_url_rule('/medical_tests/<string:patient_nat_id>/<int:test_id>', view_func=pmrm_service.medical_tests.delete_medical_test, methods=['DELETE'])

# Route bindings for TreatedBy
app.add_url_rule('/treated_by', view_func=pmrm_service.treated_by.create_treated_by, methods=['POST'])
app.add_url_rule('/treated_by/<string:patient_nat_id>/<string:doctor_nat_id>', view_func=pmrm_service.treated_by.retrieve_treated_by, methods=['GET'])
app.add_url_rule('/treated_by/<string:patient_nat_id>/<string:doctor_nat_id>', view_func=pmrm_service.treated_by.edit_treated_by, methods=['PUT'])
app.add_url_rule('/treated_by/<string:patient_nat_id>/<string:doctor_nat_id>', view_func=pmrm_service.treated_by.delete_treated_by, methods=['DELETE'])

# Start the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
