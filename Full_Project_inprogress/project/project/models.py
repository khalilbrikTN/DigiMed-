#BY : MOHAMED KHALIL BRIK
#     Rana Taher
#     Yasmina Mahdy


from django.db import models
import mysql.connector


mydb = mysql.connector.connect(
 host="mysql-yasminamahdy.alwaysdata.net" ,
 user="356122",
 password="RHus9bua7d7_*N_",
 database="yasminamahdy_digimed"
)

mycursor = mydb.cursor()

class User(models.Model):
    nat_id = models.CharField(max_length=14, primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)

class Patient(User):
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
    
    def createPatient(ValTuple):
     sql = """
     INSERT INTO patient
     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
     """ 
     try:
         mycursor.execute(sql,ValTuple)    
         mydb.commit()
     except Exception as e:
        return e
     else:
        return "Successfully created patient"

    def retrievePatient(NatID):
    sql = f"""
    SELECT * FROM patient
    WHERE NatID = {NatID}
    """
    try:
        mycursor.execute(sql)
    except e as Exception:
        return e
    else:
        result = mycursor.fetchall()
        return result[0]

    def updatePatient(NatID, fields, values):
    sql = f'''
    UPDATE patient
    SET '''
    for i in range (len(fields) - 1): 
        sql += f'''{fields[i]} = {values[i]}, '''
    sql += f'''
    {fields[-1]} = {values[-1]}
    WHERE NatID = {NatID} '''
    try:
         mycursor.execute(sql)    
         mydb.commit()
    except Exception as e:
        return e
    else:
        return f"Successfully updated patient {NatID}"

    def deletePatient(NatID):
    sql = f"""
    DELETE FROM patient
    WHERE NatID = {NatID}
    """
    try:
        mycursor.execute(sql)
        mydb.commit()
    except e as Exception:
        return e
    else:
        return f"Successfully deleted patient {NatID}"


class Doctor(User):
    specialty = models.CharField(max_length=250, null=True, blank=True)
    sub_specialty = models.CharField(max_length=250, null=True, blank=True)

    def createDoctor(ValTuple):
     sql = """
     INSERT INTO doctor
     VALUES (%s,%s,%s,%s,%s,%s)
     """ 
     try:
         mycursor.execute(sql,ValTuple)    
         mydb.commit()
     except Exception as e:
        return e
     else:
        return "Successfully created doctor"


    def retrieveDoctor(NatID):
    sql = f"""
    SELECT * FROM doctor
    WHERE NatID = {NatID}
    """
    try:
        mycursor.execute(sql)
    except e as Exception:
        return e
    else:
        result = mycursor.fetchall()
        return result

    def updateDoctor(NatID, fields, values):
    sql = f'''
    UPDATE doctor
    SET '''
    for i in range (len(fields) - 1): 
        sql += f'''{fields[i]} = {values[i]}, '''
    sql += f'''
    {fields[-1]} = {values[-1]}
    WHERE NatID = {NatID} '''
    try:
         mycursor.execute(sql)    
         mydb.commit()
    except Exception as e:
        return e
    else:
        return f"Successfully updated doctor {NatID}"

    def deleteDoctor(NatID):
    sql = f"""
    DELETE FROM doctor
    WHERE NatID = {NatID}
    """
    try:
        mycursor.execute(sql)
        mydb.commit()
    except Exception as e:
        return e
    else:
        return f"Successfully deleted doctor {NatID}"


class TreatedBy(models.Model):
    patient_nat_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="treatments")
    doctor_nat_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="patients")
    start_date = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ('patient_nat_id', 'doctor_nat_id')

    def addTreatment(treatpatient):
    sql = """
    INSERT INTO treatedby
    VALUES (%s,%s,%s)
    """
    try:
        mycursor.execute(sql,treatpatient)    
        mydb.commit()
    except Exception as e:
        return e
    else:
        return "Successfully created treatment"

    def deletetreatment(NatID,DocID):
    sql = f"""
    DELETE FROM treatedby
    WHERE PatientNatID = {NatID} and DoctorNatID = {DocID}
    """
    try:
        mycursor.execute(sql)    
        mydb.commit()
    except Exception as e:
        return e
    else:
        return "Successfully deleted treatment"

    def updatetreatment(NatID,DocID,date):
    sql = f"""
    UPDATE treatedby
    SET startDate = {date}
    WHERE PatientNatID = {NatID} and DoctorNatID = {DocID}
    """
    try:
        mycursor.execute(sql)    
        mydb.commit()
    except Exception as e:
        return e
    else:
        return "Successfully updated treatment"

    def retrievetreatment(DocID):
    sql = f"""
    SELECT * FROM treatedby
    WHERE DoctorNatID = {DocID}
    ORDER BY DoctorNatID DESC
    """
    try:
        mycursor.execute(sql)
    except Exception as e:
        return e
    else:
        result = mycursor.fetchone()
        if len(result) != 0:
            return result
        else:
            return None



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

    def addcondition(condition):
    sql = """
    INSERT INTO medicalconditions
    VALUES (%s,%s,%s)
    """
    try:
        mycursor.execute(sql,condition)    
        mydb.commit()
    except Exception as e:
        return e
    else:
        return "Successfully created condition"

    def deletecondition(NatID,Medcon,notes):
    sql = f"""
    DELETE FROM medicalconditions
    WHERE PatientNatID = {NatID} and MedCondition = {Medcon}
    and Notes = {notes}
    """
    try:
        mycursor.execute(sql)    
        mydb.commit()
    except Exception as e:
        return e
    else:
        return "Successfully deleted Condition"

    def retrievecondition(NatID):
    sql = f"""
    SELECT * FROM medicalconditions
    WHERE PatientNatID = {NatID}
    """
    try:
        mycursor.execute(sql)
    except Exception as e:
        return e
    else:
        result = mycursor.fetchone()
        if len(result) != 0:
            return result
        else:
            return None

   def UpdateCondition(NatID,condition,notes):
    sql = f"""
    UPDATE medicalconditions
    SET Notes = {notes}
    WHERE PatientNatID = {NatID} and MedCondition = {condition}
    """
    try:
        mycursor.execute(sql)    
        mydb.commit()
    except Exception as e:
        return e
    else:
        return "Successfully updated conditions"




class MedicalTests(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_tests")
    test_id = models.AutoField(primary_key=True)
    test_type = models.CharField(max_length=15, null=True, blank=True)
    subject_of_test = models.CharField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=100, null=True, blank=True)
    image_of_scan = models.CharField(max_length=50, null=True, blank=True)
    date_time_of_upload = models.DateTimeField(null=True, blank=True)

    def createTest(ValTuple):
    sql = f"""
    INSERT INTO medicaltests
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    try:
        mycursor.execute(sql,ValTuple)    
        mydb.commit()
    except Exception as e:
        return e
    else:
        return "Successfully created test"

    def deleteTest(NatID,testid):
    sql = f"""
    DELETE FROM medicaltests
    WHERE PatientNatID = {NatID} and TestID = {testid}
    """
    try:
        mycursor.execute(sql)    
        mydb.commit()
    except Exception as e:
        return e
    else:
        return "Successfully deleted test"

    def selectTest(NatID,testid,check):
    if check:
           sql = f"""
    SELECT * FROM medicaltests
    WHERE PatientNatID = {NatID}
    """
    else:
         sql = f"""
    SELECT * FROM medicaltests
    WHERE PatientNatID = {NatID} and 
    TestID = {testid}
    """
   
    try:
        mycursor.execute(sql)
    except Exception as e:
        return e
    else:
        result = mycursor.fetchone()
        if len(result) != 0:
            return result
        else:
            return None

    def updateTest(NatID,testid,result):
    sql = f"""
    UPDATE medicaltests
    SET Result = {result}
    WHERE PatientNatID = {NatID} and TestID = {testid}
    """
    try:
         mycursor.execute(sql)
         mydb.commit()
    except Exception as e:
        return e
    else:
        return f"Successfully updated doctor {NatID}"



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

    def createAppointment(ValTuple):
    sql = """
     INSERT INTO appointments
     VALUES (%s,%s,%s,%s,%s)
     """ 
    try:
        mycursor.execute(sql,ValTuple)    
        mydb.commit()
    except Exception as e:
        return e
    else:
        return "Successfully created appointment"

    def retrieveAppointment(fields, values):
    sql = """
    SELECT * FROM appointments
    WHERE """
    for i in range (len(fields) - 1): 
        sql += f'''{fields[i]} = {values[i]} AND '''
    sql += f''' {fields[-1]} = {values[-1]}'''
    try:
        mycursor.execute(sql)
    except Exception as e:
        return e
    else:
        result = mycursor.fetchall()
        return result

    def deleteAppt(DocNatID, AppID):
    sql = f"""
    DELETE FROM appointments
    WHERE DocNatID = {DocNatID} AND
    AppID = {AppID}
    """
    try:
        mycursor.execute(sql)
        mydb.commit()
    except Exception as e:
        return e
    else:
        return f"Successfully deleted Appointment"

    def updateAppt(DocNatID, AppID, fields, values):
    sql = f'''
    UPDATE appointments
    SET '''
    for i in range (len(fields) - 1): 
        sql += f'''{fields[i]} = {values[i]}, '''
    sql += f'''
    {fields[-1]} = {values[-1]}
    WHERE DocNatID = {DocNatID} AND
    AppID = {AppID}'''
    print(sql)
    try:
         mycursor.execute(sql)    
         mydb.commit()
    except Exception as e:
        return e
    else:
        return f"Successfully updated appointments"


class WorksIn(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="workplaces")
    org = models.ForeignKey(ORG, on_delete=models.CASCADE, related_name="doctors")
    schedule_working_days = models.CharField(max_length=15, null=True, blank=True)
    schedule_working_hours = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        unique_together = ('doctor', 'org')
