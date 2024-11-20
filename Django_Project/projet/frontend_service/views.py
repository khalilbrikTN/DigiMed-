
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json




# Main Apis


def main_view(request):
    return render(request, 'frontend_service/main.html')

def about_view(request):
    return render(request, 'frontend_service/about.html')

def contact_view(request):
    return render(request, 'frontend_service/contact.html')

def privacy_view(request):
    return render(request, 'frontend_service/privacy.html')

def login_view(request):
    return render(request, 'frontend_service/login.html')
