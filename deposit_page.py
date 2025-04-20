from tkinter import *
import sqlite3
from db_helper import record_transaction

def create_deposit_frame(root, prn, back_to_dashboard):
    frame = Frame(root)
    Label(frame, text="Deposit Money", font=('Arial', 16)).pack(pady=10)
    amount_entry = Entry(frame)
    amount_entry.pack()
    msg = Label(frame, text="")
    msg.pack()

    def deposit():
        amount = float(amount_entry.get())
        conn = sqlite3.connect("customers.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE customers SET balance = balance + ? WHERE prn = ?", (amount, prn))
        conn.commit()
        conn.close()
        record_transaction(prn, "Deposit", amount)
        msg.config(text="Deposited Successfully", fg="green")

    Button(frame, text="Deposit", command=deposit).pack()
    Button(frame, text="Back", command=back_to_dashboard).pack(pady=5)
    return frame

