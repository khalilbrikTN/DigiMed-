# BY : Mohamed KHALIL BRIK


from datetime import datetime
from django.db import IntegrityError
from django.db.models import Q
from .models import Appointment, Doctor, Patient, ORG


class AppointmentManager:
    def __init__(self):
        pass

    def book_appointment(self, doctor_id, patient_id, org_num, appointment_datetime):
        try:
            doctor = Doctor.objects.get(nat_id=doctor_id)
            patient = Patient.objects.get(nat_id=patient_id)
            organization = ORG.objects.get(org_no=org_num)
        except Doctor.DoesNotExist:
            return "Error: Doctor not found."
        except Patient.DoesNotExist:
            return "Error: Patient not found."
        except ORG.DoesNotExist:
            return "Error: Organization not found."

        existing_appointment = Appointment.objects.filter(
            doctor=doctor,
            app_date_time=appointment_datetime
        ).exists()

        if existing_appointment:
            return "Error: Appointment slot is already booked for this doctor."

        try:
            Appointment.objects.create(
                doctor=doctor,
                patient=patient,
                org=organization,
                app_date_time=appointment_datetime
            )
            return "Success: Appointment booked successfully."

        except IntegrityError:
            return "Error: Unable to book appointment due to a database error."

    def cancel_appointment(self, appointment_id):
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            return "Success: Appointment canceled successfully."
        except Appointment.DoesNotExist:
            return "Error: Appointment not found."
        except IntegrityError:
            return "Error: Unable to cancel appointment due to a database error."
