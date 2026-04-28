import tkinter as tk
from tkinter import messagebox

from src.backend import database_operations





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
        database_operations.insert_account(plattform, username, email, password, notes)
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
        accounts = database_operations.show_accounts()
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
            database_operations.create_db()
            database_operations.insert_master_pwd(password)
            return True

        else:
            messagebox.showerror("Error", "Password empty or doesn't match")
            return None

    def login(self, password):
        if not database_operations.check_login(password):
            messagebox.showerror("Error", "Wrong password")
            return None

        else:
            print("login success")
            return True


    def edit_account(self):
        return



    def settings_action(self):
        return