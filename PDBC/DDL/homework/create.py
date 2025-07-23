import mysql.connector

myconn=mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sp"
)
mycursor=myconn.cursor()
q1="create table student(sid int,name varchar(20),age int)"
mycursor.execute(q1)

print("Table is created Sucessfully")

mycursor.close()
myconn.close()






