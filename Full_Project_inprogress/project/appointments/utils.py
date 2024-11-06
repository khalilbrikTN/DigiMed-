# BY : Mohamed KHALIL BRIK


from datetime import datetime
from django.db import IntegrityError
from django.db.models import Q
from .models import Appointment, Doctor, Patient, ORG


def book_appointment(doctor_id, patient_id, org_num, appointment_datetime):

    # Check if the doctor, patient, and organization exist
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

    # Check if the appointment slot is already taken for the given doctor
    existing_appointment = Appointment.objects.filter(
        doctor=doctor,
        app_date_time=appointment_datetime
    ).exists()

    if existing_appointment:
        return "Error: Appointment slot is already booked for this doctor."

    # Try to create the appointment
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
