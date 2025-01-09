import mysql.connector

mydb = mysql.connector.connect(
host = "localhost", user = "root", passwd = "21102005", database="test_db"
)
print(mydb)
cursor = mydb.cursor()

cursor.execute("insert into student (name, id) values ('Bhaskar', '2')")
mydb.commit() 

print(cursor.rowcount,"detail inserted")
mydb.close()