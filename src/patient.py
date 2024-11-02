# patient_service.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import sqlite3
import datetime

app = FastAPI()

# Connect to SQLite database
conn = sqlite3.connect("appointments.db", check_same_thread=False)
cursor = conn.cursor()

# Create appointments table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS appointments (
                    doctor_id INTEGER,
                    patient_id INTEGER,
                    appointment_time TEXT
                 )''')
conn.commit()

class AppointmentRequest(BaseModel):
    doctor_id: int
    patient_id: int
    appointment_time: datetime.datetime

@app.post("/patient/request_appointment")
def request_appointment(appointment: AppointmentRequest):
    # Check doctor's availability
    cursor.execute("SELECT * FROM availability WHERE doctor_id = ? AND start_time <= ? AND end_time >= ?",
                   (appointment.doctor_id, appointment.appointment_time, appointment.appointment_time))
    availability = cursor.fetchone()
    
    if not availability:
        raise HTTPException(status_code=404, detail="Requested time is not available")

    # Book the appointment
    cursor.execute("INSERT INTO appointments (doctor_id, patient_id, appointment_time) VALUES (?, ?, ?)",
                   (appointment.doctor_id, appointment.patient_id, appointment.appointment_time))
    conn.commit()
    return {"message": "Appointment booked successfully"}

@app.get("/patient/appointments/{patient_id}")
def get_appointments(patient_id: int):
    cursor.execute("SELECT doctor_id, appointment_time FROM appointments WHERE patient_id = ?", (patient_id,))
    appointments = cursor.fetchall()
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointments found")
    return [{"doctor_id": doctor, "appointment_time": time} for doctor, time in appointments]
