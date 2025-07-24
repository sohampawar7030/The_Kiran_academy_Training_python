import mysql.connector

try:
    # Connect
    myconn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="company"
    )
    print("Connection established")

    mycursor = myconn.cursor()

#  "done"
    sql = """
    INSERT INTO Employeess (id, name, salary, department, location)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    name=VALUES(name), salary=VALUES(salary), department=VALUES(department), location=VALUES(location)
    """
    values = (3, 'Asha', 20000, 'Sales', 'Nagpur')
    mycursor.execute(sql, values)
    myconn.commit()
    print("Record inserted or updated")

    # Display records
    mycursor.execute("SELECT * FROM Employeess")
    rows = mycursor.fetchall()
    print("\nID\tName\tSalary\tDepartment\tLocation")
    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")

except mysql.connector.Error as err:
    print("Error:", err)

finally:
    if mycursor:
        mycursor.close()
    if myconn:
        myconn.close()
    print("Connection closed")
