import subprocess as sp
import pymysql
import pymysql.cursors
import datetime
from datetime import datetime, time


def delete_entry():

    try:
        print("Select which of the following tables to delete an entry from: ")
        print("Choose a table by the numbers given:\n\n")
        print("0. Patient")
        print("1. Doctors")
        print("2. Nurses")
        print("3. Appointments")

        choice = int(input("SELECT> "))
        query = ""
        query1 = ""

        if (choice == 0):
            query = "SELECT * FROM PATIENT"
            cur.execute(query)
            for row in cur:
                print(row)
                print("\n");

            PatientID = int(input("Please specify PatientID to delete: "))
            query1 = "DELETE FROM PATIENT WHERE PATIENT_ID = %d" % PatientID
            cur.execute(query1)
            con.commit()

        if (choice == 1):
            query = "SELECT * FROM DOCTORS"
            cur.execute(query)
            for row in cur:
                print(row)
                print("\n");

            DoctorID = int(input("Please specify DoctorID to delete: "))
            query1 = "DELETE FROM DOCTORS WHERE DOCTOR_ID = %d" % DoctorID
            cur.execute(query1)
            con.commit()

        if (choice == 2):
            query = "SELECT * FROM NURSES"
            cur.execute(query)
            for row in cur:
                print(row)
                print("\n");

            NurseID = int(input("Please specify NurseID to delete: "))
            query1 = "DELETE FROM NURSES WHERE NURSE_ID = %d" % NurseID
            cur.execute(query1)
            con.commit()

        if (choice == 3):
            query = "SELECT * FROM APPOINTMENTS;"
            cur.execute(query)
            for row in cur:
                print(row)
                print("\n");

            AppointmentID = int(
                input("Please specify AppointmentID to delete: "))
            query1 = "DELETE FROM APPOINTMENTS WHERE APPOINTMENT_ID = %d;" % AppointmentID
            cur.execute(query1)
            con.commit()

        print("Entry was deleted\n")

    except Exception as e:
        con.rollback()
        print("Failed to get query results")
        print(">>>>>>>>>>>>>", e)

    return


def total_cost():

    try:

        print("The total cost of all the items that need to be ordered in inventory=")
        query = "SELECT SUM(NEEDED_COUNT*PRICE) as 'Total cost' FROM INVENTORY"

        cur.execute(query)
        if cur.rowcount == 0:
            print("No records found.")

        else:
            for row in cur:
                print(row)
                print("\n");

    except Exception as e:
        con.rollback()
        print("Failed to get query results")
        print(">>>>>>>>>>>>>", e)

    return


def view():
    try:
        print("Choose the option for which details are to accessed:")
        print("1. Patients")
        print("2. Doctors")
        print("3. Appointments")
        print("4. Departments")
        print("5. Nurses")
        print("6. Services")
        print("7. Staff")
        print("8. Inventory")
        n = int(input("Enter choice> "))

        query = ""

        if n == 1:
            query = "SELECT * FROM PATIENT;"
        elif n == 2:
            query = "SELECT * FROM DOCTORS;"
        elif n == 3:
            query = "SELECT * FROM APPOINTMENTS;"
        elif n == 4:
            query = "SELECT * FROM DEPARTMENT;"
        elif n == 5:
            query = "SELECT * FROM NURSES;"
        elif n == 6:
            query = "SELECT * FROM SERVICES;"
        elif n == 7:
            query = "SELECT * FROM STAFF;"
        elif n == 8:
            query = "SELECT * FROM INVENTORY;"
        else:
            print("No/wrong option selected")
            return

        cur.execute(query)
        if cur.rowcount == 0:
            print("No records found.")

        else:
            for row in cur:
                print(row)
                print("\n");

    except Exception as e:
        con.rollback()
        print("Failed to get query results")
        print(">>>>>>>>>>>>>", e)

    return

def insert():
    try:
        print("Choose the option for which details are to accessed:")
        print("1. Patients")
        print("2. Doctors")
        print("3. Nurses")
        print("4. Appointments")
        n = int(input("Enter choice> "))
        query=""

        if n == 1:
            P_ID = int(input("Enter the patient id: "))
            F_NAME=input("Enter the patient first name: ")
            M_NAME=input("Enter the patient middle name: ")
            L_NAME=input("Enter the patient last name: ")
            ADDR=input("Enter the patient address: ")    
            date = input("Enter the date of birth (yyyy-mm-dd): ")
            Date_of_birth = datetime.date(datetime.strptime(date, "%Y-%m-%d"))
            query = "INSERT INTO `PATIENT` (PATIENT_ID, FIRST_NAME, MIDDLE_NAME, LAST_NAME, ADDRESS, DOB) VALUES(%d,'%s','%s','%s','%s','%s');" %(P_ID,F_NAME,M_NAME,L_NAME,ADDR,Date_of_birth)
    
        elif n == 2:
            Doc_ID = int(input("Enter the doctor id: "))
            Dept_id = int(input("Enter the department id: "))
            Doc_NAME = input("Enter the doctor's name: ")
            ADDS = input("Enter the doctor's address: ")
            Sal = float(input("Enter the salary: "))
            query = "INSERT INTO `DOCTORS` (DOCTOR_ID, DEPARTMENT_ID, NAME, ADDRESS, SALARY) VALUES(%d,%d,'%s','%s',%f);" %(Doc_ID,Dept_id,Doc_NAME,ADDS,Sal)

        elif n==3:
            N_ID = int(input("Enter the nurse id: "))
            Ndep_id = int(input("Enter the department id: "))
            N_NAME = input("Enter the nurse's name: ")
            ADDSS = input("Enter the nurse's address: ")
            S = float(input("Enter the salary: "))
            query = "INSERT INTO `NURSES` (NURSE_ID, DEPARTMENT_ID, NAME, ADDRESS, SALARY) VALUES(%d,%d,'%s','%s',%f);" %(N_ID,Ndep_id,N_NAME,ADDSS,S)

        elif n==4:
            A_ID = int(input("Enter the appointment id: "))
            P_ID = int(input("Enter the patient id: "))
            D_ID = int(input("Enter the doctor id: "))
            N_ID = int(input("Enter the nurse id: "))
            S_ID = int(input("Enter the service id: "))
            Time = input("Enter the date and time (yyyy-mm-dd hh:mm:ss): ")
            time = datetime.strptime(Time, "%Y-%m-%d %H:%M:%S")
            R_no = int(input("Enter the room number: "))
            query = "INSERT INTO `APPOINTMENTS` (APPOINTMENT_ID, PATIENT_ID, DOCTOR_ID, NURSE_ID, SERVICE_ID, ROOM_NUMBER, DATE_TIME) VALUES(%d,%d,%d,%d,%d,%d,'%s');" %(A_ID,P_ID,D_ID,N_ID,S_ID,R_no,time)
        
        else:
            print("No/wrong option selected")
            return

        cur.execute(query)
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to get query results")
        print(">>>>>>>>>>>>>", e)
    
    return

def update_salary():
    
    try:
        print("Select one of the following to update salary: ")
        print("Choose a table by the numbers given:\n\n")
        print("0. Doctors")
        print("1. Nurses")
        print("2. Staff")
    
        choice=int(input("SELECT> "))
        query = ""
        query1 = ""

        if (choice == 0):
            query = "SELECT * FROM DOCTORS"
            cur.execute(query)
            con.commit()

            DoctorID=int(input("Please specify DoctorID to update: "))
            Value=float(input("Please enter the new value of the salary: "))
            query1 = "UPDATE DOCTORS SET SALARY = %f WHERE DOCTOR_ID = %d" %(Value,DoctorID)
            cur.execute(query1)
            con.commit()
        
        if (choice == 1):
            query = "SELECT * FROM NURSES"
            cur.execute(query)
            con.commit()

            NurseID=int(input("Please specify NurseID to update: "))
            Value=float(input("Please enter the new value of the salary: "))
            query1 = "UPDATE NURSES SET SALARY = %f WHERE NURSE_ID = %d" %(Value,NurseID)
            cur.execute(query1)
            con.commit()

        if (choice == 2):
            query = "SELECT * FROM STAFF"
            cur.execute(query)
            con.commit()

            StaffID=int(input("Please specify StaffID to update: "))
            Value=float(input("Please enter the new value: "))
            query1 = "UPDATE STAFF SET SALARY = %f WHERE STAFF_ID = %d" %(Value,StaffID)
            cur.execute(query1)
            con.commit()
        
        print("Entry was updated\n")

    except Exception as e:
        con.rollback()
        print("Failed to get query results")
        print(">>>>>>>>>>>>>", e)


def patient_birthyr():

    try:

        yr=int(input("Enter the required birth year to get patient details> "))
        query="SELECT * FROM PATIENT where year(DOB)='%s'" % yr

        cur.execute(query)
        if cur.rowcount == 0:
            print("No records found.")

        else:
            for row in cur:
                print(row)
                print("\n");

    except Exception as e:
        con.rollback()
        print("Failed to get query results")
        print(">>>>>>>>>>>>>", e)

    return

def update_patientdetails():
    
    try:
        query = ""
        query1 = ""

        query = "SELECT * FROM PATIENT"
        cur.execute(query)
        con.commit()

        PatientID=int(input("Please specify the PatientID to update: "))
        Fname=input("Please specify the first name: ")
        Mname=input("Please specify the middle name: ")
        Lname=input("Please specify the last name: ")
        Addr=input("Please specify the address: ")
        date = input("Enter the date of birth (yyyy-mm-dd): ")
        Date_of_birth = datetime.date(datetime.strptime(date, "%Y-%m-%d"))
        query1 = "UPDATE PATIENT SET FIRST_NAME = '%s', MIDDLE_NAME = '%s', LAST_NAME = '%s', ADDRESS = '%s', DOB='%s' WHERE PATIENT_ID = %d" %(Fname,Mname,Lname,Addr,Date_of_birth,PatientID)
        cur.execute(query1)
        con.commit()
        
        print("Entry was updated\n")

    except Exception as e:
        con.rollback()
        print("Failed to get query results")
        print(">>>>>>>>>>>>>", e)

def staff_in_dept():
    
    try:

        num = int (input("Enter the department ID: "))
        query = "select sum(tbl.EachTableCount) as 'Total count' from (SELECT COUNT(*) as EachTableCount FROM DOCTORS WHERE DEPARTMENT_ID = %d UNION ALL SELECT COUNT(*) as EachTableCount FROM NURSES WHERE DEPARTMENT_ID = %d)tbl; " %(num,num)
        
        cur.execute(query)
        for row in cur:
            print(row)
            print("\n");
        con.commit()

    except Exception as e:
        con.rollback()
        print("Failed to get query results")
        print(">>>>>>>>>>>>>", e)

    return

def display_patient_name():
    
    try:
        query = "SELECT PATIENT_ID, FIRST_NAME, MIDDLE_NAME, LAST_NAME FROM PATIENT;"
        
        cur.execute(query)
        con.commit()

        if cur.rowcount==0:
            print("No records found.")
        
        else:
            for row in cur:
                print(row)
                print("\n");

    except Exception as e:
        con.rollback()
        print("Failed to get query results")
        print(">>>>>>>>>>>>>", e)

    return

def doctors_in_specialization():
    
    try:

        sp = input("Enter the Specialization name: ")
        query = "SELECT * FROM DOCTORS_SPECIALIZATION WHERE SPECIALIZATION = '%s'" %sp
        
        cur.execute(query)
        con.commit()

        if cur.rowcount==0:
            print("No records found.")
        
        else:
            for row in cur:
                print(row)
                print("\n");

    except Exception as e:
        con.rollback()
        print("Failed to get query results")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):

    if(ch == 0):
        view()
    elif(ch == 1):
        patient_birthyr()
    elif(ch == 2):
        total_cost()
    elif(ch == 3):
        delete_entry()
    elif(ch == 4):
        insert()
    elif(ch == 5):
        update_salary()
    elif(ch == 6):
        update_patientdetails()
    elif(ch == 7):
        staff_in_dept()
    elif(ch == 8):
        display_patient_name()
    elif(ch == 9):
        doctors_in_specialization()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp=sp.call('clear', shell=True)

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con=pymysql.connect(host='localhost',
                              port=30306,
                              user="root",
                              password="1234",
                              db='HOSPITAL',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp=sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp=input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp=sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("0. View details")
                print("1. Searching for details of a patient of a particular birth year")
                print("2. Total amount for items required in the inventory")
                print("3. Delete details")
                print("4. Insert details")
                print("5. Updating salary details for the staff")
                print("6. Update the details of a patient")
                print("7. Number of doctors and nurses in a department")
                print("8. Display patient details")
                print("9. Display doctors with a certain specialisation")
                print("10. Logout")
                ch=int(input("Enter choice> "))
                tmp=sp.call('clear', shell=True)
                if ch == 10:
                    exit()
                else:
                    dispatch(ch)
                    tmp=input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp=sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp=input("Enter any key to CONTINUE>")
