import mysql.connector

m=mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='sp'
)
mycursor=m.cursor()

q1="create table pwu(cid int,cname varchar(20),age int)"

mycursor.execute(q1)
print("Create Table Sucessfully !!!!!!!")
mycursor.close()
m.close()