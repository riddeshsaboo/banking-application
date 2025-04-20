from tkinter import *
import sqlite3
from qr_scanner import scan_qr_code_from_file
def create_login_frame(root, switch_to_register, switch_to_dashboard):
    frame = Frame(root)

    Label(frame, text="Login", font=('Arial', 16)).grid(row=0, column=1, pady=10)
    Label(frame, text="PRN").grid(row=1, column=0)
    Label(frame, text="Password").grid(row=2, column=0)

    prn = Entry(frame)
    password = Entry(frame, show='*')

    prn.grid(row=1, column=1)
    password.grid(row=2, column=1)

    msg = Label(frame, text="")
    msg.grid(row=4, column=1)

    def scanQR():
        qr_data = scan_qr_code_from_file()
        if qr_data:
            prn.delete(0, END)  
            prn.insert(0, qr_data)  
        else:
            msg.config(text="No QR data found or scan cancelled", fg="red")

    
    Button(frame, text="Upload QR", command=scanQR).grid(row=1, column=2, pady=5, padx=5, sticky=W)

    def login():
        conn = sqlite3.connect("customers.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE prn = ? AND password = ?", (prn.get(), password.get()))
        user = cursor.fetchone()
        conn.close()
        if user:
            switch_to_dashboard(prn.get())
        else:
            msg.config(text="Invalid Credentials", fg="red")

    Button(frame, text="Login", command=login).grid(row=3, column=1)
    Button(frame, text="Go to Register", command=switch_to_register).grid(row=5, column=1)
    return frame

