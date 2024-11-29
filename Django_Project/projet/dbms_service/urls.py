from django.urls import path

from .views import UserView
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token


urlpatterns = [
    path('User', UserView.as_view()), 
    path('create-new-User/', UserView.as_view()), # Use UserView instead of User
    path('User/<str:nat_id>/', UserView.as_view()),  # To get user by nat_id

]

# localhost:8000/api/v1.0/user/test