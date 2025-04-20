from tkinter import *
from db_helper import get_balance,get_name

def create_dashboard_frame(root, prn, switch_to_deposit, switch_to_withdraw, switch_to_pay, switch_to_txns, logout):
    frame = Frame(root)
    Label(frame, text="Dashboard", font=('Arial', 16)).pack(pady=10)
    Label(frame, text=f"Hi {get_name(prn)}", font=('Arial', 16)).pack(pady=10)
    balance_label = Label(frame, text=f"Current Balance: ₹{get_balance(prn):.2f}", font=('Arial', 14))
    balance_label.pack(pady=5)

    Button(frame, text="Deposit", command=switch_to_deposit).pack(pady=5)
    Button(frame, text="Withdraw", command=switch_to_withdraw).pack(pady=5)
    Button(frame, text="Pay to Friend", command=switch_to_pay).pack(pady=5)
    Button(frame, text="My Transactions", command=switch_to_txns).pack(pady=5)
    Button(frame, text="Logout", command=logout).pack(pady=5)

    return frame

