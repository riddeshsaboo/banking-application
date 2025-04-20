### main.py
from tkinter import *
from db_helper import init_db
from register_page import create_register_frame
from login_page import create_login_frame
from dashboard_page import create_dashboard_frame
from deposit_page import create_deposit_frame
from withdraw_page import create_withdraw_frame
from pay_page import create_pay_frame
from transactions_page import create_transactions_frame

init_db()

class App:
    def __init__(self, root):
        self.root = root
        self.prn = None
        self.frames = {}
        self.show_login()

    def clear_frames(self):
        for frame in self.frames.values():
            frame.pack_forget()
            frame.destroy()  
        self.frames.clear()  


    def show_register(self):
        self.clear_frames()
        self.frames['register'] = create_register_frame(self.root, self.show_login)
        self.frames['register'].pack()

    def show_login(self):
        self.clear_frames()
        self.frames['login'] = create_login_frame(self.root, self.show_register, self.show_dashboard)
        self.frames['login'].pack()

    def show_dashboard(self, prn):
        self.prn = prn
        self.clear_frames()
        self.frames['dashboard'] = create_dashboard_frame(self.root, prn, self.show_deposit, self.show_withdraw, self.show_pay, self.show_txns, self.show_login)
        self.frames['dashboard'].pack()

    def show_deposit(self):
        self.clear_frames()
        self.frames['deposit'] = create_deposit_frame(self.root, self.prn, lambda: self.show_dashboard(self.prn))
        self.frames['deposit'].pack()

    def show_withdraw(self):
        self.clear_frames()
        self.frames['withdraw'] = create_withdraw_frame(self.root, self.prn, lambda: self.show_dashboard(self.prn))
        self.frames['withdraw'].pack()

    def show_pay(self):
        self.clear_frames()
        self.frames['pay'] = create_pay_frame(self.root, self.prn, lambda: self.show_dashboard(self.prn))
        self.frames['pay'].pack()

    def show_txns(self):
        self.clear_frames()
        self.frames['txns'] = create_transactions_frame(self.root, self.prn, lambda: self.show_dashboard(self.prn))
        self.frames['txns'].pack()

if __name__ == '__main__':
    root = Tk()
    root.geometry("600x500")
    root.title("Customer Banking App")
    app = App(root)
    root.mainloop()
