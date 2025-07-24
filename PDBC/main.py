import mysql.connector
myconn=mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="company"
)
print("Connection is Established")
cursor=myconn.cursor()


