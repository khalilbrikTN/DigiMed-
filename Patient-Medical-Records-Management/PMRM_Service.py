#Import Flask and jsonify for API Gateway communication
from flask import Flask, request, jsonify
#Import gRPC for commmuncaiton with services
import grpc
#Import the generated gRPC classes
import PMRM_Service_pb2
import PMRM_Service_pb2_grpc
#Used for creating decoratored functions
from functools import wraps

#Initalizing the Flask app
app = Flask(__name__)

#PMRM = Patient Medical Records Management

# Helper function to check if the user is an admin 
# (SHOULD BE CHANGE TO REFLECT HOW WE ACTULLY DO IT)
#Returns True if the user is an admin, False otherwise
def is_admin(user):
    return user == "admin"

# Helper function to create the gRPC stub
def get_grpc_stub():


    #Creating the gRPC channel for communication with the database management service
    #Address is database_management_service:50051
    #Client is this service and server is the database management service
    #Insecure channel is used for simplicity for now
    channel = grpc.insecure_channel('database_management_service:50051')  
    
    #This stub allows us to call the gRPC methods on the server
    #This is also where this service will receive the responses from the server
    return PMRM_Service_pb2_grpc.PMRM_Service_Stub(channel)

@app.route('/record', methods=['POST'])
def create_record():

    
    # Handle HTTP POST request to create a new medical record.
    
    # Expects JSON data in the request, including patient_id and record data.
    # Sends a gRPC request to the Database Management Service to create the record.
    
    # Returns:
    #     JSON: Response indicating the status of the record creation.
    

    # Get the JSON data from the request (patient_id and record data)
    #From the API Gateway
    data = request.json

    #Calls the stub object to create the connection between DMS and PMRM
    stub = get_grpc_stub()

    #Creates the gRPC request object
    #So this takes the JSON and converts it to a gRPC object
    grpc_request = PMRM_Service_pb2.CreateRecordRequest(
        patient_id=data.get("patient_id"),
        data=data.get("data")
    )

    #Error handling for the gRPC request
    try:
        #Calls the CreateRecord method on the DMS
        #Response is stored in grpc_response (so the data from DMS)
        grpc_response = stub.CreateRecord(grpc_request)
        #Converts the response to JSON and returns it to the API Gateway
        return jsonify({"status": grpc_response.status, "record_id": grpc_response.record_id}), 201
    except grpc.RpcError as e:
        #Returns an error message if the gRPC request fails with details and error code
        return jsonify({"error": f"Failed to create record: {e.details()}", "code": e.code().name}), 500



@app.route('/record/<string:record_id>', methods=['GET'])
def retrieve_record(record_id):
    stub = get_grpc_stub()
    grpc_request = PMRM_Service_pb2.RetrieveRecordRequest(record_id=record_id)
    try:
        grpc_response = stub.RetrieveRecord(grpc_request)
        return jsonify({
            "status": grpc_response.status,
            "record_id": grpc_response.record_id,
            "patient_id": grpc_response.patient_id,
            "data": grpc_response.data
        })
    except grpc.RpcError as e:
        return jsonify({"error": f"Failed to retrieve record: {e.details()}", "code": e.code().name}), 500



@app.route('/record/<string:record_id>', methods=['PUT'])
def edit_record(record_id):
    data = request.json
    stub = get_grpc_stub()
    grpc_request = PMRM_Service_pb2.UpdateRecordRequest(
        record_id=record_id,
        new_data=data.get("new_data")
    )
    try:
        grpc_response = stub.UpdateRecord(grpc_request)
        return jsonify({"status": grpc_response.status, "record_id": grpc_response.record_id})
    except grpc.RpcError as e:
        return jsonify({"error": f"Failed to update record: {e.details()}", "code": e.code().name}), 500




def require_admin(f):

    
    # Decorator function to restrict access to admin users.
    
    # This decorator checks the user's role (passed in request headers) and ensures
    # only admins can access the decorated endpoint.
    
    # Args:
    #     f (function): The function to be wrapped by this decorator.
    
    # Returns:
    #     function: The wrapped function with admin check.
    
    @wraps(f)
    def wrapper(*args, **kwargs):

        # Get the user's role from the request headers. Default to "user" if not provided.
        user_role = request.headers.get("Role", "user")
        
        #Prevent non-admins from accessing the endpoint
        if user_role != "admin":
            return jsonify({"error": "Unauthorized access - Admins only"}), 403
        #If the user is an admin, call the original function
        return f(*args, **kwargs)
    return wrapper

@app.route('/record/<string:record_id>', methods=['DELETE'])
@require_admin
def delete_record(record_id):
    stub = get_grpc_stub()
    grpc_request = PMRM_Service_pb2.DeleteRecordRequest(record_id=record_id)
    try:
        grpc_response = stub.DeleteRecord(grpc_request)
        return jsonify({"status": grpc_response.status, "record_id": grpc_response.record_id})
    except grpc.RpcError as e:
        return jsonify({"error": f"Failed to delete record: {e.details()}", "code": e.code().name}), 500


#Allows the app to reveive requests from the API Gateway 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
