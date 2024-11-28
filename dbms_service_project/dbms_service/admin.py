from django.contrib import admin
from .models import Patient, MedicalCondition, MedicalTest

admin.site.register(Patient)
admin.site.register(MedicalCondition)
admin.site.register(MedicalTest)