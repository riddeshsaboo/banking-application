import sqlite3
import random
import string
from datetime import datetime

def init_db():
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fname TEXT NOT NULL,
            lname TEXT NOT NULL,
            prn TEXT UNIQUE NOT NULL,
            aadhar TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            custID TEXT UNIQUE NOT NULL,
            balance REAL DEFAULT 0
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prn TEXT,
            type TEXT,
            amount REAL,
            to_prn TEXT,
            date_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def generate_random_id(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def record_transaction(prn, type_, amount, to_prn=None):
    from datetime import datetime
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        "INSERT INTO transactions (prn, type, amount, to_prn, date_time) VALUES (?, ?, ?, ?, ?)",
        (prn, type_, amount, to_prn, now)
    )

    if type_ == "Pay" and to_prn:
        cursor.execute(
            "INSERT INTO transactions (prn, type, amount, to_prn, date_time) VALUES (?, ?, ?, ?, ?)",
            (to_prn, "Received from Friend", amount, prn, now)
        )

    conn.commit()
    conn.close()

def get_balance(prn):
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM customers WHERE prn = ?", (prn,))
    bal = cursor.fetchone()[0]
    conn.close()
    return bal

def get_name(prn):
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT fname FROM customers WHERE prn = ?", (prn,))
    fname = cursor.fetchone()[0]
    conn.close()
    return fname
