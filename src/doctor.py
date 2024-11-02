# doctor_service.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3
import datetime

app = FastAPI()

# Connect to SQLite database
conn = sqlite3.connect("appointments.db", check_same_thread=False)
cursor = conn.cursor()

# Create availability table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS availability (
                    doctor_id INTEGER,
                    start_time TEXT,
                    end_time TEXT
                 )''')
conn.commit()

class Availability(BaseModel):
    doctor_id: int
    start_time: datetime.datetime
    end_time: datetime.datetime

@app.post("/doctor/availability")
def set_availability(avail: Availability):
    cursor.execute("INSERT INTO availability (doctor_id, start_time, end_time) VALUES (?, ?, ?)",
                   (avail.doctor_id, avail.start_time, avail.end_time))
    conn.commit()
    return {"message": "Availability set successfully"}

@app.get("/doctor/availability/{doctor_id}", response_model=List[Availability])
def get_availability(doctor_id: int):
    cursor.execute("SELECT start_time, end_time FROM availability WHERE doctor_id = ?", (doctor_id,))
    availability = cursor.fetchall()
    if not availability:
        raise HTTPException(status_code=404, detail="No availability found for this doctor")
    return [{"doctor_id": doctor_id, "start_time": start, "end_time": end} for start, end in availability]
