import tkinter as tk
from src.backend import controller, database_operations


class Actions:

    def __init__(self, main_ui, popup_ui):
        self.listbox = None
        self.main_ui = main_ui
        self.popup_ui = popup_ui
        self.controller = controller

    # Function login action for button
    def login_action(self):
        pwd = self.main_ui.master_password.get().strip()
        success = controller.login(pwd)
        if success:
            self.main_ui.show_screen("menu")

    def register_action(self):
        pwd = self.main_ui.master_password.get().strip()
        confirm_pwd = self.main_ui.master_password_confirm.get().strip()
        success = controller.register(pwd, confirm_pwd)
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



    def show_account_action(self):
        accounts = database_operations.show_accounts()
        self.main_ui.accounts = accounts
        # Empty list before reload
        self.main_ui.listbox.delete(0, tk.END)
        for account in accounts:
            self.main_ui.listbox.insert(tk.END, f"Plattform: {account[1]} |Username: {account[2]} |Email: {account[3]} |Password: "
                                        f"{account[4]} |Notes: {account[5]}")
        return


    def settings_action(self):
        return