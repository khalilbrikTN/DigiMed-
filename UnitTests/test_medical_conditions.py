import unittest
from unittest.mock import MagicMock, patch
from flask import json
from PMRM_Service import app, MedicalConditions, PMRM_Service_pb2

class TestMedicalConditionsService(unittest.TestCase):
    @patch('PMRM_Service.PMRM_Service_pb2_grpc.PMRMServiceStub')
    def setUp(self, mock_stub):
        # Initialize the test client
        self.app = app.test_client()
        self.app.testing = True
        
        # Mock the gRPC stub and methods
        self.mock_stub = mock_stub.return_value
        self.mock_create_medical_condition = self.mock_stub.CreateMedicalCondition
        self.mock_create_medical_condition.return_value.status = "Success"

    def test_create_medical_condition(self):
        # Define the test data for the request
        test_data = {
            "PatientNatID": "123456789",
            "MedCondition": "Hypertension",
            "Notes": "Patient has a history of hypertension."
        }
        
        # Make a POST request to the endpoint
        response = self.app.post(
            '/medical_conditions',
            data=json.dumps(test_data),
            content_type='application/json'
        )
        
        # Check that gRPC was called with the expected parameters
        self.mock_create_medical_condition.assert_called_once_with(
            PMRM_Service_pb2.CreateMedicalConditionRequest(
                table_name="MedicalConditions",
                PatientNatID="123456789",
                MedCondition="Hypertension",
                Notes="Patient has a history of hypertension."
            )
        )
        
        # Check the response status code and data
        self.assertEqual(response.status_code, 201)
        response_data = json.loads(response.data)
        self.assertEqual(response_data["status"], "Success")

if __name__ == '__main__':
    unittest.main()
