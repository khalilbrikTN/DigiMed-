from django.http import JsonResponse

class RoleBasedAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip validation for homepage
        if request.path == '/':
            return self.get_response(request)

        # Extract role and NatID
        role = request.GET.get('role')
        nat_id = request.GET.get('nat_id')

        # Validate presence of Role and NatID
        if not role or not nat_id:
            return JsonResponse({'error': 'Role and NatID are required'}, status=400)

        # Attach role and NatID to the request for views
        request.user_role = role
        request.user_nat_id = nat_id
        return self.get_response(request)
