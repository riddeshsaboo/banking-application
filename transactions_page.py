from tkinter import *
import sqlite3

def create_transactions_frame(root, prn, back_to_dashboard):
    frame = Frame(root)
    Label(frame, text="My Transactions", font=('Arial', 16)).pack(pady=10)

    listbox = Listbox(frame, width=60)
    listbox.pack()

    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT type, amount, to_prn, date_time FROM transactions WHERE prn = ? ORDER BY id DESC", (prn,))
    for row in cursor.fetchall():
        t_type, amount, to_prn, date_time = row

        if t_type == "Pay" and to_prn:
            line = f"{date_time} - Sent ₹{amount} to Friend {to_prn}"
        elif t_type == "Received from Friend" and to_prn:
            line = f"{date_time} - Received ₹{amount} from Friend {to_prn}"
        else:
            line = f"{date_time} - {t_type} ₹{amount}"

        listbox.insert(END, line)
    conn.close()

    Button(frame, text="Back", command=back_to_dashboard).pack(pady=5)
    return frame

