import mysql.connector
me=mysql.connector.connect(
  host='localhost',
  user='root',
  password='root',
  database='sp'
)
myc=me.cursor()

q2="insert  into pwu values(1,'pawar',20)"
myc.execute(q2)
me.commit()

myc.close()
