#Pre requirement
#install mysql-connector using pip command
#install mysql in the system
#create a database named employee
#update the user and password(line 15 and 16)as required
#create a table named empDetails with following conditions
#eID int primary key, Fname varchar(255), Lname varchar(255),Email varchar(255),Phone varchar(15)
#Address varchar(255),Gender varchar(1)

import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="employee",
)

mycursor=mydb.cursor()
print("CONNECTION ESTABLISHED SUCCESSFULLY\n")

def showAllDetails():
    mycursor.execute("SELECT *FROM empdetails")
    result=mycursor.fetchall()
    for x in result:
        print("_"*50,"\n")
        print("eID : ",x[0])
        print("First Name : ",x[1])
        print("Last Name : ",x[2])
        print("Email : ",x[3])
        print("Phone : ",x[4])
        print("Address : ",x[5])
        print("Gender : ",x[6])
    print("_"*50,"\n")

def showParticular(column):
    mycursor.execute("SELECT "+column+" from empdetails")
    result=mycursor.fetchall()
    return result

def insertData():
    print("\nINSERTION OF DATA")
    print("_"*50,"\n")
    eid=int(input("Enter the Employee ID: "))
    fname=input("Enter the First Name: ")
    lname=input("Enter the Last Name: ")
    email=input("Enter the Email Address: ")
    phone=int(input("Enter the Phone Number: "))
    address=input("Enter the Address: ")
    gender=input("Enter the Gender: ")
    
    eid_detail=showParticular("eid")
    for i in eid_detail:
        if(eid==i[0]):
            print("Employee with eid",eid,"already exists")
            return
    sql="INSERT INTO empdetails (eID,Fname,Lname,Email,Phone,Address,Gender) VALUES(%(EID)s, %(FNAME)s, %(LNAME)s, %(EMAIL)s, %(PHONE)s, %(ADDRESS)s, %(GENDER)s)"
    val={
        "EID":eid,
        "FNAME":fname,
        "LNAME":lname,
        "EMAIL":email,
        "PHONE":phone,
        "ADDRESS":address,
        "GENDER":gender,
    }
    mycursor.execute(sql,val)
    mydb.commit()
    print("Data entered successfully")

def deleteData():
    eid=int(input("Enter the Employee ID: "))
    eid_detail=showParticular("eid")
    for i in eid_detail:
        if(i[0]==eid):
            sql="DELETE FROM empDetails WHERE eid = %(EID)s"
            val={
                "EID":eid,
            }
            mycursor.execute(sql,val)
            print("Data deleted Successfully")
            mydb.commit()
            return
    print("Employee ID not found!!")

def updateData():
    eid=int(input("Enter the Employee ID: "))
    eid_detail=showParticular("eid")
    for i in eid_detail:
        if(i[0]==eid):
            print("UPDATE: ")
            print("1. EID")
            print("2. First Name")
            print("3. Last Name")
            print("4. Email Address")
            print("5. Phone")
            print("6. Address")
            print("7. Gender")
            print("8. Cancel")
            uchoice=int(input("Enter your choice: "))
            if uchoice==1:
                column="eID"
                udata=input("Enter the data to be updated: ")
            elif uchoice==2:
                column="Fname"
                udata=input("Enter the data to be updated: ")
            elif uchoice==3:
                column="Lname"
                udata=input("Enter the data to be updated: ")
            elif uchoice==4:
                column="Email"
                udata=input("Enter the data to be updated: ")
            elif uchoice==5:
                column="Phone"
                udata=input("Enter the data to be updated: ")
            elif uchoice==6:
                column="Address"
                udata=input("Enter the data to be updated: ")
            elif uchoice==7:
                column="Gender"
                udata=input("Enter the data to be updated: ")
            elif uchoice==8:
                print("Cancelled")
                break
            else:
                print("Invalid Input!!Cancelling")
                break
            sql="UPDATE empDetails SET "+column+" = %(UDATA)s WHERE eID = %(DATA)s"
            val={
                "UDATA":udata,
                "DATA":eid,
            }
            mycursor.execute(sql,val)
            mydb.commit()
            print("Data updated successfully")
            return
    print("Employee ID not found")

def searchData():
    print("\nSEARCH DATA")
    eid=int(input("Enter the Employee ID: "))
    eid_detail=showParticular("eid")
    for i in eid_detail:
        if(i[0]==eid):
            sql="SELECT *FROM empDetails WHERE eID = %(EID)s"
            val={
                "EID":eid
            }
            mycursor.execute(sql,val)
            result=mycursor.fetchall()
            for x in result:
                print("_"*50,"\n")
                print("eID : ",x[0])
                print("First Name : ",x[1])
                print("Last Name : ",x[2])
                print("Email : ",x[3])
                print("Phone : ",x[4])
                print("Address : ",x[5])
                print("Gender : ",x[6])
            print("_"*50,"\n")
            return
    print("Employee ID not found")
            
while(1):
    print("_"*50,"\n")
    print("1. Show All Details")
    print("2. Insert Details")
    print("3. Delete Details")
    print("4. Update Details")
    print("5. Search Details")
    print("6. Exit Program")
    print("_"*50,"\n")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("\nEMPLOYEE DETAILS :")
        showAllDetails()
        
    elif choice==2:
        insertData()
    
    elif choice==3:
        deleteData()
        
    elif choice==4:
        updateData()
    
    elif choice==5:
        searchData()
    
    elif choice==6:
        print("\nExited Successfully")
        break
    else:
        print("\nInvalid Input")
        continue
mydb.close()