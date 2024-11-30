from django.http import JsonResponse

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip validation for homepage
        if request.path == '/':
            return self.get_response(request)

        # Extract role, NatID, and DoctorID
        role = request.GET.get('role')
        nat_id = request.GET.get('nat_id')
        doctor_id = request.GET.get('doctor_id')

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

        # Attach role and IDs to the request for views
        request.user_role = role
        request.user_nat_id = nat_id
        request.user_doctor_id = doctor_id

        return self.get_response(request)