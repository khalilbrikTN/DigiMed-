from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password



class User(models.Model):
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
    password = models.CharField(max_length=128)  # Store hashed passwords

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}"

class Patient(User):
    blood_type = models.CharField(max_length=3, null=True, blank=True)
    height = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    weight = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return f"Patient: {self.first_name} {self.last_name}"

    @classmethod
    def create_patient(cls, nat_id, first_name, last_name, password, middle_name=None, street=None, 
                       region=None, city=None, phone_number=None, email=None, gender=None, dob=None, 
                       blood_type=None, height=None, weight=None):
        try:
            # Create a Patient instance (inherits from User)
            patient = cls.objects.create(
                nat_id=nat_id,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                street=street,
                region=region,
                city=city,
                phone_number=phone_number,
                email=email,
                gender=gender,
                dob=dob,
                blood_type=blood_type,
                height=height,
                weight=weight,
            )

            # Set and save the hashed password
            patient.set_password(password)
            patient.save()

            return patient
        except Exception as e:
            return f"Error creating patient: {e}"


    @classmethod
    def retrieve_patient(cls, nat_id):
        try:
            patient = Patient.objects.get(nat_id=nat_id)
            return patient
        except Patient.DoesNotExist:
            return f"No patient found with ID {nat_id}"
        except Exception as e:
            return f"Error retrieving patient: {e}"

    @classmethod
    def update_patient(cls, nat_id, **kwargs):
        try:
            patient = Patient.objects.get(nat_id=nat_id)
            user = patient.user
            user.first_name = kwargs.get('first_name', user.first_name)
            user.middle_name = kwargs.get('middle_name', user.middle_name)
            user.last_name = kwargs.get('last_name', user.last_name)
            user.save()

            for field, value in kwargs.items():
                if hasattr(patient, field):
                    setattr(patient, field, value)
            patient.save()
            return f"Successfully updated patient {nat_id}"
        except Patient.DoesNotExist:
            return f"No patient found with ID {nat_id}"
        except Exception as e:
            return f"Error updating patient: {e}"

    @classmethod
    def delete_patient(cls, nat_id):
        try:
            patient = Patient.objects.get(nat_id=nat_id)
            patient.delete()
            return f"Successfully deleted patient {nat_id}"
        except Patient.DoesNotExist:
            return f"No patient found with ID {nat_id}"
        except Exception as e:
            return f"Error deleting patient: {e}"

class Doctor(User):
    specialty = models.CharField(max_length=250, null=True, blank=True)
    sub_specialty = models.CharField(max_length=250, null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    clinic_address = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"Doctor: {self.first_name} {self.last_name} (Specialty: {self.specialty})"

    @classmethod
    def create_doctor(cls, nat_id, first_name, last_name, password, middle_name=None, street=None, region=None,
                      city=None, phone_number=None, email=None, gender=None, dob=None, specialty=None,
                      sub_specialty=None, years_of_experience=None, clinic_address=None):
        try:
            # Create a Doctor instance (inherits from User)
            doctor = cls.objects.create(
                nat_id=nat_id,
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                street=street,
                region=region,
                city=city,
                phone_number=phone_number,
                email=email,
                gender=gender,
                dob=dob,
                specialty=specialty,
                sub_specialty=sub_specialty,
                years_of_experience=years_of_experience,
                clinic_address=clinic_address,
            )

            # Set and save the hashed password
            doctor.set_password(password)
            doctor.save()

            return doctor
        except Exception as e:
            return f"Error creating doctor: {e}"

    @classmethod
    def retrieve_doctor(cls, nat_id):
        try:
            doctor = cls.objects.get(nat_id=nat_id)
            return doctor
        except cls.DoesNotExist:
            return f"No doctor found with ID {nat_id}"
        except Exception as e:
            return f"Error retrieving doctor: {e}"

    @classmethod
    def update_doctor(cls, nat_id, **kwargs):
        try:
            doctor = cls.objects.get(nat_id=nat_id)
            user = doctor.user

            # Update User fields
            user.first_name = kwargs.get('first_name', user.first_name)
            user.middle_name = kwargs.get('middle_name', user.middle_name)
            user.last_name = kwargs.get('last_name', user.last_name)
            user.street = kwargs.get('street', user.street)
            user.region = kwargs.get('region', user.region)
            user.city = kwargs.get('city', user.city)
            user.phone_number = kwargs.get('phone_number', user.phone_number)
            user.email = kwargs.get('email', user.email)
            user.gender = kwargs.get('gender', user.gender)
            user.dob = kwargs.get('dob', user.dob)
            user.save()

            # Update Doctor fields
            for field, value in kwargs.items():
                if hasattr(doctor, field):
                    setattr(doctor, field, value)
            doctor.save()

            return f"Successfully updated doctor {nat_id}"
        except cls.DoesNotExist:
            return f"No doctor found with ID {nat_id}"
        except Exception as e:
            return f"Error updating doctor: {e}"

    @classmethod
    def delete_doctor(cls, nat_id):
        try:
            doctor = cls.objects.get(nat_id=nat_id)
            doctor.delete()
            return f"Successfully deleted doctor {nat_id}"
        except cls.DoesNotExist:
            return f"No doctor found with ID {nat_id}"
        except Exception as e:
            return f"Error deleting doctor: {e}"

class Appointment(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.RESTRICT, related_name="appointments")
    app_id = models.AutoField(primary_key=True)
    app_date_time = models.DateTimeField(null=True, blank=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="appointments")

    def create_appointment(self, **kwargs):

        try:
            appointment = Appointment.objects.create(**kwargs)
            return appointment
        except Exception as e:
            return f"Error creating appointment: {e}"

    def retrieve_appointments(self, **filters):

        try:
            appointments = Appointment.objects.filter(**filters)
            return appointments
        except Exception as e:
            return f"Error retrieving appointments: {e}"

    def update_appointment(self, app_id, **kwargs):

        try:
            Appointment.objects.filter(app_id=app_id).update(**kwargs)
            return f"Successfully updated appointment {app_id}"
        except Appointment.DoesNotExist:
            return f"No appointment found with ID {app_id}"
        except Exception as e:
            return f"Error updating appointment: {e}"

    def delete_appointment(self, app_id):

        try:
            appointment = Appointment.objects.get(app_id=app_id)
            appointment.delete()
            return f"Successfully deleted appointment {app_id}"
        except Appointment.DoesNotExist:
            return f"No appointment found with ID {app_id}"
        except Exception as e:
            return f"Error deleting appointment: {e}"
        
class MedicalCondition(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="medical_conditions")
    med_condition = models.CharField(max_length=14)
    notes = models.CharField(max_length=500)

    class Meta:
        unique_together = ('patient', 'med_condition')

    def create_condition(self, patient, med_condition, notes):

        try:
            condition = MedicalCondition.objects.create(
                patient=patient,
                med_condition=med_condition,
                notes=notes
            )
            return condition
        except Exception as e:
            return f"Error creating condition: {e}"

    def delete_condition(self, patient, med_condition, notes):

        try:
            condition = MedicalCondition.objects.get(
                patient=patient,
                med_condition=med_condition,
                notes=notes
            )
            condition.delete()
            return "Successfully deleted condition"
        except MedicalCondition.DoesNotExist:
            return "Condition not found"
        except Exception as e:
            return f"Error deleting condition: {e}"

    def retrieve_conditions(self, patient):

        try:
            conditions = MedicalCondition.objects.filter(patient=patient)
            return conditions
        except Exception as e:
            return f"Error retrieving conditions: {e}"
        
class MedicalTest(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="medical_tests")
    test_id = models.AutoField(primary_key=True)
    test_type = models.CharField(max_length=15, null=True, blank=True)
    subject_of_test = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=100, null=True, blank=True)
    image_of_scan = models.CharField(max_length=50, null=True, blank=True)
    date_time_of_upload = models.DateTimeField(null=True, blank=True)

    def create_test(self, **kwargs):

        try:
            test = MedicalTest.objects.create(**kwargs)
            return test
        except Exception as e:
            return f"Error creating test: {e}"

    def delete_test(self, patient, test_id):

        try:
            test = MedicalTest.objects.get(patient=patient, test_id=test_id)
            test.delete()
            return "Successfully deleted test"
        except MedicalTest.DoesNotExist:
            return "Test not found"
        except Exception as e:
            return f"Error deleting test: {e}"

    def select_tests(self, patient, test_id=None):

        try:
            if test_id:
                tests = MedicalTest.objects.filter(patient=patient, test_id=test_id)
            else:
                tests = MedicalTest.objects.filter(patient=patient)
            return tests
        except Exception as e:
            return f"Error retrieving tests: {e}"

    def update_test_result(self, patient, test_id, result):

        try:
            MedicalTest.objects.filter(patient=patient, test_id=test_id).update(result=result)
            return "Successfully updated test result"
        except MedicalTest.DoesNotExist:
            return "Test not found"
        except Exception as e:
            return f"Error updating test result: {e}"

class TreatmentAssignment(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name="treatment_assignments")
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name="assigned_patients")
    start_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('patient', 'doctor')
        verbose_name = "Treatment Assignment"
        verbose_name_plural = "Treatment Assignments"

    def add_treatment(self, patient, doctor, start_date=None):

        try:
            assignment = TreatmentAssignment.objects.create(
                patient=patient,
                doctor=doctor,
                start_date=start_date
            )
            return assignment
        except Exception as e:
            return f"Error creating treatment assignment: {e}"

    def delete_treatment(self, patient, doctor):

        try:
            assignment = TreatmentAssignment.objects.get(patient=patient, doctor=doctor)
            assignment.delete()
            return "Successfully deleted treatment assignment"
        except TreatmentAssignment.DoesNotExist:
            return "Treatment assignment not found"
        except Exception as e:
            return f"Error deleting treatment assignment: {e}"

    def update_treatment_start_date(self, patient, doctor, start_date):

        try:
            TreatmentAssignment.objects.filter(patient=patient, doctor=doctor).update(start_date=start_date)
            return "Successfully updated treatment start date"
        except TreatmentAssignment.DoesNotExist:
            return "Treatment assignment not found"
        except Exception as e:
            return f"Error updating treatment assignment: {e}"

    def retrieve_treatments_for_doctor(self, doctor):

        try:
            assignments = TreatmentAssignment.objects.filter(doctor=doctor).order_by('patient')
            return assignments
        except Exception as e:
            return f"Error retrieving treatment assignments: {e}"
        
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="prescriptions")
    prescription_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT, null=True, blank=True, related_name="prescriptions")
    date_of_prescription = models.DateField(null=True, blank=True)

    def get_patient(self):
        return self.patient

    def set_patient(self, patient):
        self.patient = patient

    def get_doctor(self):
        return self.doctor

    def set_doctor(self, doctor):
        self.doctor = doctor

    def get_date_of_prescription(self):
        return self.date_of_prescription

    def set_date_of_prescription(self, date):
        self.date_of_prescription = date

class Medicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name="medicines")
    medicine_name = models.CharField(max_length=35)
    subscription_heading = models.CharField(max_length=2, null=True, blank=True)
    form_of_intake = models.CharField(max_length=25, null=True, blank=True)
    duration_of_intake = models.IntegerField(null=True, blank=True)
    frequency_of_intake = models.CharField(max_length=25, null=True, blank=True)

    class Meta:
        unique_together = ('prescription', 'medicine_name')

    
    def get_prescription(self):
        return self.prescription

    def set_prescription(self, prescription):
        self.prescription = prescription

    def get_medicine_name(self):
        return self.medicine_name

    def set_medicine_name(self, name):
        self.medicine_name = name

    def get_subscription_heading(self):
        return self.subscription_heading

    def set_subscription_heading(self, heading):
        self.subscription_heading = heading

    def get_form_of_intake(self):
        return self.form_of_intake

    def set_form_of_intake(self, form):
        self.form_of_intake = form

    def get_duration_of_intake(self):
        return self.duration_of_intake

    def set_duration_of_intake(self, duration):
        self.duration_of_intake = duration

    def get_frequency_of_intake(self):
        return self.frequency_of_intake

    def set_frequency_of_intake(self, frequency):
        self.frequency_of_intake = frequency

class Referral(models.Model):
    referring_doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT, related_name="referrals_given")
    referred_doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT, related_name="referrals_received")
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT, related_name="referrals")

    class Meta:
        unique_together = ('referring_doctor', 'referred_doctor', 'patient')

    def get_referring_doctor(self):
        return self.referring_doctor

    def set_referring_doctor(self, doctor):
        self.referring_doctor = doctor

    def get_referred_doctor(self):
        return self.referred_doctor

    def set_referred_doctor(self, doctor):
        self.referred_doctor = doctor

    def get_patient(self):
        return self.patient

    def set_patient(self, patient):
        self.patient = patient

class ORG(models.Model):
    org_no = models.AutoField(primary_key=True)
    org_name = models.CharField(max_length=150)
    opening_details = models.CharField(max_length=300)
    notes = models.CharField(max_length=500, null=True, blank=True)

    def get_org_name(self):
        return self.org_name

    def set_org_name(self, name):
        self.org_name = name

    def get_opening_details(self):
        return self.opening_details

    def set_opening_details(self, details):
        self.opening_details = details

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

class ORGLocation(models.Model):
    org = models.ForeignKey(ORG, on_delete=models.CASCADE, related_name="locations")
    location = models.CharField(max_length=250)

    class Meta:
        unique_together = ('org', 'location')

    class Meta:
        unique_together = ('org', 'location')

    def get_org(self):
        return self.org

    def set_org(self, org):
        self.org = org

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

class DoctorWorkingDays(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="workplaces")
    org = models.ForeignKey(ORG, on_delete=models.CASCADE, related_name="doctors")
    schedule_working_days = models.CharField(max_length=15, null=True, blank=True)
    schedule_working_hours = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        unique_together = ('doctor', 'org')


    def get_doctor(self):
        return self.doctor

    def set_doctor(self, doctor):
        self.doctor = doctor

    def get_org(self):
        return self.org

    def set_org(self, org):
        self.org = org

    def get_schedule_working_days(self):
        return self.schedule_working_days

    def set_schedule_working_days(self, days):
        self.schedule_working_days = days

    def get_schedule_working_hours(self):
        return self.schedule_working_hours

    def set_schedule_working_hours(self, hours):
        self.schedule_working_hours = hours