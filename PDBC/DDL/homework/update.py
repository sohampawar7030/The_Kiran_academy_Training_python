import mysql.connector

myconn=mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='sp'
)

print("Connection established sucessfully !!!!!!! ")

mycursor=myconn.cursor()

q2="insert into student values(2,'omi',100)"


mycursor.execute(q2)

myconn.commit()


print("Data Inserted Sucessfully !!!!!!!")


mycursor.close()
myconn.close()