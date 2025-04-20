from tkinter import *
import sqlite3
from db_helper import record_transaction

def create_withdraw_frame(root, prn, back_to_dashboard):
    frame = Frame(root)
    Label(frame, text="Withdraw Money", font=('Arial', 16)).pack(pady=10)
    amount_entry = Entry(frame)
    amount_entry.pack()
    msg = Label(frame, text="")
    msg.pack()

    def withdraw():
        try:
            amount = float(amount_entry.get())

            conn = sqlite3.connect("customers.db")
            cursor = conn.cursor()

            cursor.execute("SELECT balance FROM customers WHERE prn = ?", (prn,))
            current_balance = cursor.fetchone()[0]

            if amount > current_balance:
                msg.config(text="Insufficient Funds", fg="red")
            else:
                cursor.execute("UPDATE customers SET balance = balance - ? WHERE prn = ?", (amount, prn))
                conn.commit()

                record_transaction(prn, "Withdraw", amount)
                msg.config(text="Withdrawn Successfully", fg="green")
        except Exception as e:
            msg.config(text=str(e), fg="red")
        finally:
            conn.close()

    Button(frame, text="Withdraw", command=withdraw).pack()
    Button(frame, text="Back", command=back_to_dashboard).pack(pady=5)
    return frame
