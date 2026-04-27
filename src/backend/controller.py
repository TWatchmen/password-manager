from tkinter import messagebox

from src.backend import database_operations
from src.ui import main_window
from src.ui.main_window import *


def register(password, confirm_password):#
    if password and password == confirm_password:
        print("master pw")
        database_operations.create_db()
        database_operations.insert_master_pwd(password)
        return True

    else:
        messagebox.showerror("Error", "Password empty or doesn't match")
        return None


def login(password):
    if not database_operations.check_login(password):
        messagebox.showerror("Error", "Wrong password")
        return None

    else:
        print("login success")
        return True

def handle_open_account(listbox, accounts, open_account_window):
    selection = listbox.curselection()

    if selection:
        index = selection[0]
        account = accounts[index]
        account_id = account[0]

        open_account_window(account_id)
