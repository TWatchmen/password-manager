import secrets
import string
import random
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import INSERT

from src.backend import database_actions
from src.backend.database_actions import show_accounts
from src.ui import popup_window


class Actions:

    def __init__(self, main_ui, popup_ui):
        self.listbox = None
        self.main_ui = main_ui
        self.popup_ui = popup_ui

    # Function login action for button
    def login_action(self):
        pwd = self.main_ui.master_password.get().strip()
        success = self.login(pwd)
        if success:
            self.main_ui.show_screen("menu")

    def register_action(self):
        pwd = self.main_ui.master_password.get().strip()
        confirm_pwd = self.main_ui.master_password_confirm.get().strip()
        success = self.register(pwd, confirm_pwd)
        if success:
            self.main_ui.show_screen("login")

    def add_account(self, plattform, username, email, password, notes):
        database_actions.insert_account(plattform, username, email, password, notes)
        print("add success")
        return True


    # Function adding action to the button
    def add_account_action(self):

        # Debug print
        print(self.popup_ui.plattform_entry)


        plattform = self.popup_ui.plattform_entry.get().strip()
        username = self.popup_ui.username_entry.get().strip()
        email = self.popup_ui.email_entry.get().strip()
        password = self.popup_ui.password_entry.get().strip()
        notes = self.popup_ui.notes_entry.get().strip()
        self.add_account(plattform, username, email, password, notes)
        self.popup_ui.popup.destroy()
        self.show_account_action()
        self.main_ui.show_screen("menu")

    def handle_open_account(self, listbox, accounts, open_account_window):
        selection = listbox.curselection()

        if selection:
            index = selection[0]
            account = accounts[index]
            account_id = account.id

            open_account_window(account_id)

    def show_account_action(self):
        accounts = database_actions.show_accounts()
        self.main_ui.accounts = accounts
        # Empty list before reload
        self.main_ui.listbox.delete(0, tk.END)
        for account in accounts:
            self.main_ui.listbox.insert(tk.END, f"Plattform: {account.plattform} |Username: {account.username} |Email: {account.email} |Password: "
                                        f"{account.password} |Notes: {account.notes}")

        return

    def register(self, password, confirm_password):  #
        if password and password == confirm_password:
            print("master pw")
            database_actions.create_db()
            database_actions.insert_master_pwd(password)
            return True

        else:
            messagebox.showerror("Error", "Password empty or doesn't match")
            return None

    def login(self, password):
        if not database_actions.check_login(password):
            messagebox.showerror("Error", "Wrong password")
            return None

        else:
            print("login success")
            return True


    def edit_account(self,account_id, plattform, username, email, password, notes):
        database_actions.save_account(account_id, plattform, username, email, password, notes)
        self.popup_ui.popup.destroy()
        self.show_account_action()
        return None

    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        random_password = "".join(random.choice(characters) for _ in range(12))

        self.popup_ui.password_entry.delete(0, tk.END)
        self.popup_ui.password_entry.insert(INSERT, random_password)
        self.popup_ui.security.check_password_strength()

        return None





    def settings_action(self):
        return