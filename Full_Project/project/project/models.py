#BY : MOHAMED KHALIL BRIK


from django.db import models

class Patient(models.Model):
    nat_id = models.CharField(max_length=14, primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    street = models.CharField(max_length=250, null=True, blank=True)
    region = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=17, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    blood_type = models.CharField(max_length=3, null=True, blank=True)
    height = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)



class Doctor(models.Model):
    nat_id = models.CharField(max_length=14, primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=250, null=True, blank=True)
    sub_specialty = models.CharField(max_length=250, null=True, blank=True)


class TreatedBy(models.Model):
    patient_nat_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="treatments")
    doctor_nat_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patients")
    start_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('patient_nat_id', 'doctor_nat_id')



class ORG(models.Model):
    org_no = models.AutoField(primary_key=True)
    org_name = models.CharField(max_length=150)
    opening_details = models.CharField(max_length=300)
    notes = models.CharField(max_length=500, null=True, blank=True)



class ORGLocation(models.Model):
    org = models.ForeignKey(ORG, on_delete=models.CASCADE, related_name="locations")
    location = models.CharField(max_length=250)

    class Meta:
        unique_together = ('org', 'location')


class MedicalConditions(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_conditions")
    med_condition = models.CharField(max_length=14)
    notes = models.CharField(max_length=500)

    class Meta:
        unique_together = ('patient', 'med_condition')



class MedicalTests(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_tests")
    test_id = models.AutoField(primary_key=True)
    test_type = models.CharField(max_length=15, null=True, blank=True)
    subject_of_test = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=100, null=True, blank=True)
    image_of_scan = models.CharField(max_length=50, null=True, blank=True)
    date_time_of_upload = models.DateTimeField(null=True, blank=True)


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="prescriptions")
    prescription_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT, null=True, blank=True, related_name="prescriptions")
    date_of_prescription = models.DateField(null=True, blank=True)


class Medicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name="medicines")
    medicine_name = models.CharField(max_length=35)
    subscription_heading = models.CharField(max_length=2, null=True, blank=True)
    form_of_intake = models.CharField(max_length=25, null=True, blank=True)
    duration_of_intake = models.IntegerField(null=True, blank=True)
    frequency_of_intake = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        unique_together = ('prescription', 'medicine_name')

class Referring(models.Model):
    referring_doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT, related_name="referrals_given")
    referred_doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT, related_name="referrals_received")
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT, related_name="referrals")

    class Meta:
        unique_together = ('referring_doctor', 'referred_doctor', 'patient')


    
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT, related_name="appointments")
    app_id = models.AutoField(primary_key=True)
    org = models.ForeignKey(ORG, on_delete=models.RESTRICT, null=True, blank=True, related_name="appointments")
    app_date_time = models.DateTimeField(null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")


class WorksIn(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="workplaces")
    org = models.ForeignKey(ORG, on_delete=models.CASCADE, related_name="doctors")
    schedule_working_days = models.CharField(max_length=15, null=True, blank=True)
    schedule_working_hours = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        unique_together = ('doctor', 'org')
