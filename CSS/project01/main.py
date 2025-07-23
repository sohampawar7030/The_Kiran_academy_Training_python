import tkinter as tk
from tkinter import messagebox  
import mysql.connector

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # change this if your user is different
        password="1234",          # add your MySQL password here
        database="contact_db"
    )

# Insert data into the database
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    message = entry_message.get("1.0", tk.END).strip()

    if name == "" or email == "" or message == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    try:
        db = connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
        val = (name, email, message)
        cursor.execute(sql, val)
        db.commit()
        db.close()
        messagebox.showinfo("Success", "Contact submitted successfully!")
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_message.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Database Error", str(e))

# GUI
root = tk.Tk()
root.title("Contact Form")
root.geometry("400x300")

tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root, width=50)
entry_name.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root, width=50)
entry_email.pack()

tk.Label(root, text="Message").pack()
entry_message = tk.Text(root, height=5, width=38)
entry_message.pack()

tk.Button(root, text="Submit", command=submit_form).pack(pady=10)

root.mainloop()
