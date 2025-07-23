import mysql.connector
myconn=mysql.connector.Connect(
  host='localhost',
  user='root',
  password='root',
  database='sp'
)
myCousor=myconn.cursor()

val=int(input("Enter the Id : "))
val2=input('enter the car name :' )
val3=int(input('Enter the value : '))

abc=(val,val2,val3,)

q=(f"insert  into car values(%s,%s,%s)")

myCousor.execute(q,abc)
myconn.commit()
print("data is Import Sucessfully !!!!!!")

myCousor.close()
myconn.close()
