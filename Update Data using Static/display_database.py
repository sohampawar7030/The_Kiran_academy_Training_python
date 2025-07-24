import mysql.connector
myconn=mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='sp'
)

myCorsor=myconn.cursor()

q="select * from car"

myCorsor.execute(q)

for i in myCorsor :
  print(f"the car id is {i[0]} and car name is {i[1]} and price is {i[2]} ")


myCorsor.close()
myconn.close()
