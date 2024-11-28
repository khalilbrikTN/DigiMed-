# dbms_service/serializers.py

from rest_framework import serializers
from .models import (
    User, Patient, Doctor, MedicalCondition, MedicalTest,
    TreatmentAssignment, Appointment, Prescription, Medicine,
    Referral, ORG, ORGLocation, DoctorWorkingDays
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

# dbms_service/serializers.py

from rest_framework import serializers
from .models import MedicalCondition, Patient

class MedicalConditionSerializer(serializers.ModelSerializer):
    PatientNatID = serializers.SlugRelatedField(
        queryset=Patient.objects.all(),
        slug_field='nat_id',
        source='patient'
    )
    MedCondition = serializers.CharField(source='med_condition')
    Notes = serializers.CharField(source='notes')

    class Meta:
        model = MedicalCondition
        fields = ['PatientNatID', 'MedCondition', 'Notes']
        validators = []


class MedicalTestSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
        queryset=Patient.objects.all(),
        slug_field='nat_id'
    )

    class Meta:
        model = MedicalTest
        fields = '__all__'
        validators = []  # Disable unique_together validation

class TreatmentAssignmentSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
        queryset=Patient.objects.all(),
        slug_field='nat_id'
    )
    doctor = serializers.SlugRelatedField(
        queryset=Doctor.objects.all(),
        slug_field='nat_id'
    )

    class Meta:
        model = TreatmentAssignment
        fields = '__all__'
        validators = []

class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
        queryset=Patient.objects.all(),
        slug_field='nat_id'
    )
    doctor = serializers.SlugRelatedField(
        queryset=Doctor.objects.all(),
        slug_field='nat_id'
    )

    class Meta:
        model = Appointment
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
        queryset=Patient.objects.all(),
        slug_field='nat_id'
    )
    doctor = serializers.SlugRelatedField(
        queryset=Doctor.objects.all(),
        slug_field='nat_id'
    )

    class Meta:
        model = Prescription
        fields = '__all__'

class MedicineSerializer(serializers.ModelSerializer):
    prescription = serializers.PrimaryKeyRelatedField(
        queryset=Prescription.objects.all()
    )

    class Meta:
        model = Medicine
        fields = '__all__'
        validators = []

class ReferralSerializer(serializers.ModelSerializer):
    referring_doctor = serializers.SlugRelatedField(
        queryset=Doctor.objects.all(),
        slug_field='nat_id'
    )
    referred_doctor = serializers.SlugRelatedField(
        queryset=Doctor.objects.all(),
        slug_field='nat_id'
    )
    patient = serializers.SlugRelatedField(
        queryset=Patient.objects.all(),
        slug_field='nat_id'
    )

    class Meta:
        model = Referral
        fields = '__all__'
        validators = []

class ORGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ORG
        fields = '__all__'

class ORGLocationSerializer(serializers.ModelSerializer):
    org = serializers.PrimaryKeyRelatedField(
        queryset=ORG.objects.all()
    )

    class Meta:
        model = ORGLocation
        fields = '__all__'
        validators = []

class DoctorWorkingDaysSerializer(serializers.ModelSerializer):
    doctor = serializers.SlugRelatedField(
        queryset=Doctor.objects.all(),
        slug_field='nat_id'
    )
    org = serializers.PrimaryKeyRelatedField(
        queryset=ORG.objects.all()
    )

    class Meta:
        model = DoctorWorkingDays
        fields = '__all__'
        validators = []
