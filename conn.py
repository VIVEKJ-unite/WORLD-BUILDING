import mysql.connector

mydb = mysql.connector.connect(
host = "localhost", user = "root", passwd = "21102005", database="test_db"
)
print(mydb)
cursor = mydb.cursor()
cursor.execute("create database college;")
cursor.execute("create table Student(name varchar(255) NULL, enrollment int not null);")

def create_student(name, enrollment):
    query = "insert into Student(name, enrollment) values(%s,%s)"
    values = (name, enrollment):
    cursor.execute(query,values)
    mydb.commit()
    print(f"User (name) added succesfully!")

def read_students():
    cursor.execute()

def update_student (name, new_enrollment):
    query = "update student set enrollment  = %s where name = %s "
    values = (new_enrollment,name)
    cursor.execute(query, values)
    mydb.commit()

def delete student(enrollment):
    query = "delete from student where enrollment_number = %s"
    cursor.execute (query , (enrollment))
    mydb.commit()

create_student("Ram", 123)
create_student("Shayam", 456)
create_student("Param", 789)

print("Students after update operation:")
read_students()

delete_student
