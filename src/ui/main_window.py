import tkinter as tk
from src.backend import database_operations
from src.services.actions import Actions
from src.ui import popup_window
from src.ui.popup_window import PopupWindow
from src.utils.security import PasswordSecurity

# Ui


class MainWindow:
    def __init__(self, root, main_ui, popup_ui, start_screen = "welcome"):
        # generate root window

        self.password_strength_indicator_3 = None
        self.password_strength_indicator_2 = None
        self.password_strength_indicator_1 = None
        self.password_strength_indicator = None
        self.button_close = None
        self.button_open = None
        self.accounts = None
        self.popup_account = None
        self.root = root
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)
        self.root.title("Password Manager")
        self.popup_window = PopupWindow(self.root)
        self.security = PasswordSecurity(self.popup_window)
        self.popup_window.security = self.security
        self.actions = Actions(self, self.popup_window)
        self.ui = popup_window
        self.password_label = None
        self.notes_label = None
        self.email_label = None
        self.username_label = None
        self.plattform_label = None
        self.button_login = None
        self.add_label = None
        self.button_save = None
        self.popup = None
        self.button_settings = None
        self.button_add = None
        self.listbox = None
        self.scrollbar = None
        self.table_frame = None
        self.button_register = None
        self.login_label = None

        self.master_password = None
        self.master_password_confirm = None

        if start_screen == "welcome":
            self.show_screen("welcome")
        elif start_screen == "login":
            self.show_screen("login")


    # Welcome (start window) user interface
    # if no database exists in path
    def welcome_window(self):
        tk.Label(self.root, text="Welcome to your Password Manager", font=("Arial", 18)) \
            .place(relx=0.5, rely=0.3, anchor="center")
        tk.Label(self.root, text="Create your own Master Password. Don't forget your Password!", font=("Arial", 10))\
        .place(relx=0.5, rely=0.35, anchor="center")

        self.master_password = tk.Entry(self.root, font=("Arial", 10), show="*")
        self.master_password.place(relx=0.5, rely=0.4, anchor="center", width=200)
        self.master_password_confirm = tk.Entry(self.root, font=("Arial", 10), show="*")
        self.master_password_confirm.place(relx=0.5, rely=0.45, anchor="center", width=200)


        self.button_register = tk.Button(self.root, text="Register", command=self.actions.register_action)
        self.button_register.place(relx=0.5, rely=0.5, anchor="center")

    # Login user interface
    def login_window(self):
        self.login_label = tk.Label(self.root, text="Login", font=("Arial", 15))
        self.login_label.place(relx=0.5, rely=0.35, anchor="center")

        self.master_password = tk.Entry(self.root, font=("Arial", 10), show="*")
        self.master_password.place(relx=0.5, rely=0.4, anchor="center", width=200)

        self.button_login = tk.Button(self.root, text="Login", command=self.actions.login_action)
        self.button_login.place(relx=0.5, rely=0.5, anchor="center")

    # Menu user interface
    def menu_window(self):
        self.login_label = tk.Label(self.root, text="Password Manager ", font=("Arial", 18))
        self.login_label.place(relx=0.5, rely=0.05, anchor="center")

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        # Define Listbox
        self.listbox = tk.Listbox(self.root, width=60, height=15, font=("Arial", 15),
                                  yscrollcommand=self.scrollbar.set)
        self.listbox.place(relx=0.5, rely=0.1, anchor="n")

        # Connect scrollbar with listbox
        self.scrollbar.config(command=self.listbox.yview)

        # Button for adding new Accounts
        self.button_add = tk.Button(self.root, text="Add Account", command=self.add_account_window)
        self.button_add.place(relx=0.15, rely=0.85, anchor="s")

        # Button for changing entry
        self.button_open = tk.Button(self.root, text="Open",
                                    command=lambda: self.actions.handle_open_account(self.listbox, self.accounts, self.open_account_window))
        self.button_open.place(relx=0.3, rely=0.85, anchor="s")

        """
        # Button for settings
        self.button_settings = tk.Button(self.root, text="Settings", bg="lightgrey", fg="black",
                                         command=self.actions.settings_action)
        self.button_settings.place(relx=0.9, rely=0.85, anchor="s")
        """

        self.actions.show_account_action()




    def add_account_window(self):
        self.popup = self.popup_window.create_popup(title="Add Account")




        # Button for saving entries in database
        self.button_save = tk.Button(self.popup, text="Save", command=self.actions.add_account_action)
        self.button_save.place(relx=0.5, rely=0.8, anchor="center")





    def open_account_window(self, account_id = None):

        self.popup = self.popup_window.create_popup(title="Account")

        # Button for saving entries in database
        self.button_save = tk.Button(self.popup, text="Save",
                                     command=lambda: self.actions.edit_account(account_id,
                                        self.popup_window.plattform_entry.get().strip(),
                                        self.popup_window.username_entry.get().strip(),
                                        self.popup_window.email_entry.get().strip(),
                                        self.popup_window.password_entry.get().strip(),
                                        self.popup_window.notes_entry.get().strip()))
        self.button_save.place(relx=0.4, rely=0.8, anchor="center")


        self.button_close = tk.Button(self.popup, text="Close",
                                     command=lambda: self.popup.destroy())
        self.button_close.place(relx=0.6, rely=0.8, anchor="center")

        if account_id is not None:
            account = database_operations.select_account(account_id)

            if account:
                self.popup_window.plattform_entry.insert(0, account.plattform)
                self.popup_window.username_entry.insert(0, account.username)
                self.popup_window.email_entry.insert(0, account.email)
                self.popup_window.password_entry.insert(0, account.password)
                self.popup_window.notes_entry.insert(0, account.notes)
        self.popup_window.security.check_password_strength()



    def show_screen(self, screen_name):
        self.clear_window()

        if screen_name == "welcome":
            self.welcome_window()
        elif screen_name == "login":
            self.login_window()
        elif screen_name == "menu":
            self.menu_window()

    # Function clearing window
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()



