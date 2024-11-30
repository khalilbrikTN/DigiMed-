# pmrm_frontend/middleware.py

from django.http import JsonResponse

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Define paths to exempt from role checking
        self.exempt_paths = [
            '/medical_conditions/',  # CRUD operations for medical conditions
            '/medical_tests/',       # CRUD operations for medical tests
            '/treated_by/',          # CRUD operations for treated_by relationships
        ]

    def __call__(self, request):
        # Normalize the request path (remove trailing slashes for consistency)
        path = request.path.rstrip('/')

        # Skip validation for homepage and exempt paths
        if path == '' or any(path.startswith(exempt_path.rstrip('/')) for exempt_path in self.exempt_paths):
            return self.get_response(request)

        # Extract role, NatID, and DoctorID based on the request method
        if request.method == 'GET':
            role = request.GET.get('role')
            nat_id = request.GET.get('nat_id')
            doctor_id = request.GET.get('doctor_id')
        else:
            role = request.POST.get('role')
            nat_id = request.POST.get('nat_id')
            doctor_id = request.POST.get('doctor_id')

        # Debugging: Print extracted values (remove or comment out in production)
        print(f"Middleware - Role: {role}, NatID: {nat_id}, DoctorID: {doctor_id}")

        # Validate presence of Role
        if not role:
            return JsonResponse({'error': 'Role is required'}, status=400)

        # Validate Role-specific fields
        if role == 'patient' and not nat_id:
            return JsonResponse({'error': 'Role and NatID are required for patients'}, status=400)

        if role == 'doctor' and not doctor_id:
            return JsonResponse({'error': 'Role and DoctorID are required for doctors'}, status=400)

        # No validation needed for admin role
        if role == 'admin':
            pass  # Admin does not require additional IDs

        # Attach role and IDs to the request for views (optional, based on your requirements)
        request.user_role = role
        request.user_nat_id = nat_id
        request.user_doctor_id = doctor_id

        return self.get_response(request)