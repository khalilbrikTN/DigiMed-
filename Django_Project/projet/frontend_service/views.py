
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json




# Main Apis


def main_view(request):
    return render(request, 'frontend_service/main.html')