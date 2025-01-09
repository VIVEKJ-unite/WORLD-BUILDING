import mysql.connector

def LoginData():

    mydb = mysql.connector.connect(host = "localhost" , user = "root", passwd = "21102005",database="login_data")
    print(mydb)
    cursor = mydb.cursor()

    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    phone = int(input("Enter your phone number: "))
    gender = input("Enter your gender(M/F): ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")

    query = ("insert into data (FIRSTNAME,LASTNAME,PHONE_NUMBER,GENDER,DOB) values (%(FIRSTNAME)s,%(LASTNAME)s,%(PHONE_NUMBER)d,%(GENDER)s,%(DOB)s)")
    val = {"FIRSTNAME" : fname,
           "LASTNAME" : lname,
           "PHONE_NUMBER" : phone, 
           "GENDER" : gender,
           "DOB" : dob}
    cursor.execute(query,val)
    mydb.commit()
    print("data successfully inserted")
    mydb.close()

LoginData()