from tkinter import *
import sqlite3
from db_helper import record_transaction, get_balance
from qr_scanner import scan_qr_code_from_file
def create_pay_frame(root, prn, back_to_dashboard):
    frame = Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=10)

    Label(frame, text="Pay to Friend", font=('Arial', 16)).grid(row=0, column=0, columnspan=2, pady=10)
    Label(frame, text="Enter the PRN of your friend or upload their QR", font=('Arial', 12)).grid(row=1, column=0, columnspan=2, pady=5)

    Label(frame, text="Enter the PRN:").grid(row=2, column=0, sticky=W, padx=5)
    to_prn_entry = Entry(frame)
    to_prn_entry.grid(row=2, column=1, padx=5, pady=5)

    Label(frame, text="Enter the Amount to Pay:").grid(row=3, column=0, sticky=W, padx=5)
    amount_entry = Entry(frame)
    amount_entry.grid(row=3, column=1, padx=5, pady=5)

    def scanQR():
        qr_data = scan_qr_code_from_file()
        if qr_data:
            to_prn_entry.delete(0, END)  
            to_prn_entry.insert(0, qr_data)  
        else:
            msg.config(text="No QR data found or scan cancelled", fg="red")

    Button(frame, text="Upload QR", command=scanQR).grid(row=4, column=1, pady=5, padx=5, sticky=W)

    msg = Label(frame, text="", font=('Arial', 10))
    msg.grid(row=5, column=0, columnspan=2, pady=5)

    def pay():
        try:
            to_prn = to_prn_entry.get().strip()
            amount = float(amount_entry.get().strip())

            if not to_prn:
                msg.config(text="Recipient PRN is required", fg="red")
                return
            if not amount or amount <= 0:
                msg.config(text="Enter a valid positive amount", fg="red")
                return
            if to_prn == prn:
                msg.config(text="Cannot pay yourself", fg="red")
                return

            sender_balance = get_balance(prn)
            if sender_balance < amount:
                msg.config(text="Insufficient Balance", fg="red")
                return

            conn = sqlite3.connect("customers.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customers WHERE prn = ?", (to_prn,))
            recipient = cursor.fetchone()

            if not recipient:
                msg.config(text="Recipient not found", fg="red")
                conn.close()
                return

            cursor.execute("UPDATE customers SET balance = balance - ? WHERE prn = ?", (amount, prn))
            cursor.execute("UPDATE customers SET balance = balance + ? WHERE prn = ?", (amount, to_prn))
            conn.commit()
            conn.close()

            
            record_transaction(prn, "Pay", amount, to_prn)
            msg.config(text="Payment successful!", fg="green")
        except ValueError:
            msg.config(text="Enter valid numeric values", fg="red")
        except Exception as e:
            msg.config(text=f"Error: {str(e)}", fg="red")

    
    Button(frame, text="Pay", command=pay).grid(row=6, column=0, pady=5, padx=5, sticky=E)
    Button(frame, text="Back", command=back_to_dashboard).grid(row=6, column=1, pady=5, padx=5, sticky=W)

    return frame
