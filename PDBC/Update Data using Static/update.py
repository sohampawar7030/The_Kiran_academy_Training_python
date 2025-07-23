import mysql.connector
myconn=mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='sp'
)

myCorsor=myconn.cursor()

val1=int(input('Enter the Id : '))
val2=input('Enter the car name :')

abc=(val2,val1,)

q="update car set name =%s where cid = %s "

myCorsor.execute(q,abc)

print("data is Update Sucessfully !!! ")

myconn.commit()
myCorsor.close()
myconn.close()