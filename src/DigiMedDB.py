import mysql.connector
mycursor = mydb.cursor()

mydb = mysql.connector.connect(
 host="mysql-yasminamahdy.alwaysdata.net" ,
 user="356122",
 password="RHus9bua7d7_*N_",
 database="yasminamahdy_digimed"
)

def createPatient(Patient):
     sql = """
     INSERT INTO patient
     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
     """ 
     try:
         mycursor.execute(sql,Patient)    
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
    
    def createDoctor(Doctor):
     sql = """
     INSERT INTO doctor
     VALUES (%s,%s,%s,%s,%s,%s)
     """ 
     try:
         mycursor.execute(sql,Doctor)    
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
    
def createAppointment(Appt):
    sql = """
     INSERT INTO appointments
     VALUES (%s,%s,%s,%s,%s)
     """ 
    try:
        mycursor.execute(sql,Appt)    
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
    
def createTest(Medicaltest):
    sql = f"""
    INSERT INTO medicaltests
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    """
    try:
        mycursor.execute(sql,Medicaltest)    
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