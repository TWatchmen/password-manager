import tkinter as tk
from src.backend import controller, db_logic


class Actions:
    def __init__(self, ui):
        self.ui = ui
        self.controller = controller

    # Function login action for button
    def login_action(self):
        pwd = self.ui.master_password.get().strip()
        success = controller.login(pwd)
        if success:
            self.ui.show_screen("menu")

    def register_action(self):
        pwd = self.ui.master_password.get().strip()
        confirm_pwd = self.ui.master_password_confirm.get().strip()
        controller.register(pwd, confirm_pwd)

        success = controller.register(pwd, confirm_pwd)
        if success:
            self.ui.show_screen("login")

    # Function adding action to the button
    def add_account_action(self):
        plattform = self.ui.plattform_entry.get().strip()
        username = self.ui.username_entry.get().strip()
        email = self.ui.email_entry.get().strip()
        password = self.ui.password_entry.get().strip()
        notes = self.ui.notes_entry.get().strip()
        controller.add_account(plattform, username, email, password, notes)
        self.ui.popup.destroy()
        self.ui.show_account_action()
        self.ui.show_screen("menu")


    def show_account_action(self):
        accounts = db_logic.show_accounts()

        for account in accounts:
            self.ui.listbox.insert(tk.END, f"Plattform: {account[1]} |Username: {account[2]} |Email: {account[3]} |Password: "
                                        f"{account[4]} |Notes: {account[5]}")
        return


    def settings_action(self):
        return