from tkinter import messagebox

from src.backend import db_logic
from src.ui import main_window
from src.ui.main_window import *


def register(password, confirm_password):#
    if password and password == confirm_password:
        print("master pw")
        db_logic.create_db()
        db_logic.insert_master_pwd(password)
        return True

    else:
        messagebox.showerror("Error", "Password empty or doesn't match")

def login(password):
    if not db_logic.check_login(password):
        messagebox.showerror("Error", "Wrong password")
        return None

    else:
        print("login success")
        return True


def add_account():
    return 

