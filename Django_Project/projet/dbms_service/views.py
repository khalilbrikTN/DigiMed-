from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password  # For hashing passwords
from .models import User  # Import the User model
from django.db import IntegrityError  # Handle unique constraint issues

class UserView(APIView):
    def get(self, request, nat_id=None, format=None):
        try:
            if nat_id:  # If 'nat_id' is provided as part of the path
                user = User.objects.filter(nat_id=nat_id).first()  # Retrieve the user by nat_id
                if not user:  # If no user is found with the given nat_id
                    return Response(
                        {"error": f"No user found with National ID: {nat_id}."},
                        status=status.HTTP_404_NOT_FOUND
                    )
                
                user_dict = {
                    user.nat_id: {
                        'first_name': user.first_name,
                        'middle_name': user.middle_name,
                        'last_name': user.last_name,
                        'street': user.street,
                        'region': user.region,
                        'city': user.city,
                        'phone_number': user.phone_number,
                        'email': user.email,
                        'gender': user.gender,
                        'dob': user.dob,
                    }
                }

            else:  # If no 'nat_id' is provided, return all users
                user_objects = User.objects.all()
                user_dict = {
                    user.nat_id: {
                        'first_name': user.first_name,
                        'middle_name': user.middle_name,
                        'last_name': user.last_name,
                        'street': user.street,
                        'region': user.region,
                        'city': user.city,
                        'phone_number': user.phone_number,
                        'email': user.email,
                        'gender': user.gender,
                        'dob': user.dob,
                    }
                    for user in user_objects
                }

            return Response(user_dict, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        try:
            users = request.data.get('users', [])  # Extract the list of users
            if not isinstance(users, list):
                return Response(
                    {"error": "Invalid format. 'users' must be a list."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            created_users = []
            for user_data in users:
                # Validate mandatory fields
                required_fields = ['nat_id', 'first_name', 'last_name', 'password']
                missing_fields = [field for field in required_fields if not user_data.get(field)]
                if missing_fields:
                    return Response(
                        {"error": f"Missing required fields: {', '.join(missing_fields)}"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                # Create user object
                try:
                    user = User.objects.create(
                        nat_id=user_data['nat_id'],
                        first_name=user_data['first_name'],
                        middle_name=user_data.get('middle_name', ''),
                        last_name=user_data['last_name'],
                        street=user_data.get('street', ''),
                        region=user_data.get('region', ''),
                        city=user_data.get('city', ''),
                        phone_number=user_data.get('phone_number', ''),
                        email=user_data.get('email', ''),
                        gender=user_data.get('gender', ''),
                        dob=user_data.get('dob'),
                        password=make_password(user_data['password']),  # Hash password
                    )
                    user.save()

                    created_users.append({
                        'nat_id': user.nat_id,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'email': user.email,
                    })
                except IntegrityError as e:
                    return Response(
                        {"error": f"User with nat_id '{user_data['nat_id']}' already exists."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                except Exception as e:
                    return Response(
                        {"error": f"Failed to create user: {str(e)}"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            return Response({"created_users": created_users}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
