from tkinter import *
import sqlite3
from db_helper import generate_random_id
from qr_generator import generate_qr
from tkinter import messagebox

def create_register_frame(root, switch_to_login):
    frame = Frame(root)

    Label(frame, text="Register", font=('Arial', 16)).grid(row=0, column=1, pady=10)
    Label(frame, text="First Name").grid(row=1, column=0)
    Label(frame, text="Last Name").grid(row=2, column=0)
    Label(frame, text="PRN").grid(row=3, column=0)
    Label(frame, text="Aadhar").grid(row=4, column=0)
    Label(frame, text="Password").grid(row=5, column=0)

    fname = Entry(frame)
    lname = Entry(frame)
    prn = Entry(frame)
    aadhar = Entry(frame)
    password = Entry(frame, show='*')

    fname.grid(row=1, column=1)
    lname.grid(row=2, column=1)
    prn.grid(row=3, column=1)
    aadhar.grid(row=4, column=1)
    password.grid(row=5, column=1)

    msg = Label(frame, text="")
    msg.grid(row=7, column=1)

    def register():
        try:
            conn = sqlite3.connect("customers.db")
            cursor = conn.cursor()
            cust_id = generate_random_id()
            cursor.execute('''INSERT INTO customers (fname, lname, prn, aadhar, password, custID)
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (fname.get(), lname.get(), prn.get(), aadhar.get(), password.get(), cust_id))
            conn.commit()
            conn.close()
            try:
                generate_qr(prn.get())
                messagebox.showinfo("Your account is Created Successfully ","Qr is saved , you can use it for login and payments")
            except Exception as e :
                messagebox.showinfo("Error",e)
            msg.config(text="Registered Successfully! Redirecting...", fg="green")
            switch_to_login()
        except Exception as e:
            msg.config(text=str(e), fg="red")

    Button(frame, text="Register", command=register).grid(row=6, column=1)
    Button(frame, text="Go to Login", command=switch_to_login).grid(row=8, column=1)
    return frame

