import mysql.connector
myconn=mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='sp'
)
print("connection Suceessfully")

myCursor=myconn.cursor()

myCursor.execute('create table car(cid int,name varchar(20),price int)')

print("The Table is Created Sucessfully")
myCursor.close()
myconn.close()
