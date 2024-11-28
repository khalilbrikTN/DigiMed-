# dbms_service/serializers.py

from rest_framework import serializers
from .models import MedicalCondition, Patient, MedicalTest, TreatmentAssignment, Doctor

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


class MedicalConditionSerializer(serializers.ModelSerializer):
    PatientNatID = serializers.SlugRelatedField(
        queryset=Patient.objects.all(),
        slug_field='nat_id',
        source='patient'
    )
    MedCondition = serializers.CharField(source='med_condition')
    Notes = serializers.CharField(source='notes', required=False, allow_blank=True)

    class Meta:
        model = MedicalCondition
        fields = ['PatientNatID', 'MedCondition', 'Notes']
        validators = []

    def update(self, instance, validated_data):
        # Update each field explicitly
        if 'patient' in validated_data:
            instance.patient = validated_data['patient']
        if 'med_condition' in validated_data:
            instance.med_condition = validated_data['med_condition']
        if 'notes' in validated_data:
            instance.notes = validated_data['notes']
        instance.save()
        return instance



class MedicalTestSerializer(serializers.ModelSerializer):
    PatientNatID = serializers.SlugRelatedField(
        queryset=Patient.objects.all(),
        slug_field='nat_id',
        source='patient'  # Maps to the 'patient' ForeignKey in the model
    )
    TestID = serializers.IntegerField(source='test_id', read_only=True)
    Test_Type = serializers.CharField(source='test_type', required=False, allow_blank=True)
    SubjectOfTest = serializers.CharField(source='subject_of_test', required=False, allow_blank=True)
    Result = serializers.CharField(source='result', required=False, allow_blank=True)
    ImageOfScan = serializers.CharField(source='image_of_scan', required=False, allow_blank=True)
    Date_TimeOfUpload = serializers.DateTimeField(source='date_time_of_upload', required=False)

    class Meta:
        model = MedicalTest
        fields = [
            'PatientNatID', 'TestID', 'Test_Type', 
            'SubjectOfTest', 'Result', 'ImageOfScan', 'Date_TimeOfUpload'
        ]



class TreatedBySerializer(serializers.ModelSerializer):
    PatientNatID = serializers.SlugRelatedField(
        queryset=Patient.objects.all(),
        slug_field='nat_id',
        source='patient'  # Maps to the 'patient' ForeignKey in the model
    )
    DoctorNatID = serializers.SlugRelatedField(
        queryset=Doctor.objects.all(),
        slug_field='nat_id',
        source='doctor'  # Maps to the 'doctor' ForeignKey in the model
    )
    start_Date = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = TreatmentAssignment
        fields = ['PatientNatID', 'DoctorNatID', 'start_date']





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
