import tkinter as tk
from operator import length_hint
from src.backend import database_operations
from src.backend import controller, database_operations
from src.services import actions
from src.services.actions import Actions
from src.ui import popup_window
from src.ui.popup_window import PopupWindow


class MainWindow:
    def __init__(self, root, start_screen = "welcome"):
        # generate root window
        self.accounts = None
        self.popup_account = None
        self.root = root
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)
        self.root.title("Password Manager")
        self.actions = Actions(self)
        self.popup_window = PopupWindow(self.root)
        self.password_label = None
        self.notes_label = None
        self.email_label = None
        self.username_label = None
        self.plattform_label = None
        self.button_login = None
        self.add_label = None
        self.username_entry = None
        self.notes_entry = None
        self.password_entry = None
        self.plattform_entry = None
        self.email_entry = None
        self.button_save = None
        self.popup = None
        self.button_settings = None
        self.button_add = None
        self.listbox = None
        self.scrollbar = None
        self.table_frame = None
        self.button_register = None
        self.login_label = None
        #self.root.configure(background="light grey")

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
        self.button_add = tk.Button(self.root, text="Open",
                                    command=lambda: controller.handle_open_account(self.listbox, self.accounts, self.open_account_window))
        self.button_add.place(relx=0.3, rely=0.85, anchor="s")


        # Button for settings
        self.button_settings = tk.Button(self.root, text="Settings", bg="lightgrey", fg="black",
                                         command=self.actions.settings_action)
        self.button_settings.place(relx=0.9, rely=0.85, anchor="s")

        self.actions.show_account_action()




    def add_account_window(self):
        self.popup = self.popup_window.create_popup(title="Add Account")

        # Headline
        self.add_label = tk.Label(self.popup, text="Add Account", font=("Arial", 15))
        self.add_label.place(relx=0.5, rely=0.05, anchor="center")

        # Plattform label and entry
        self.plattform_label = tk.Label(self.popup, text="Plattform", font=("Arial", 10))
        self.plattform_label.place(relx=0.4, rely=0.15, anchor="center")
        self.plattform_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.plattform_entry.place(relx=0.5, rely=0.2, anchor="center", width=250)

        # Username label and entry
        self.username_label = tk.Label(self.popup, text="Username", font=("Arial", 10))
        self.username_label.place(relx=0.4, rely=0.25, anchor="center")
        self.username_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.username_entry.place(relx=0.5, rely=0.3, anchor="center", width=250)

        # Email label and entry
        self.email_label = tk.Label(self.popup, text="Email", font=("Arial", 10))
        self.email_label.place(relx=0.4, rely=0.35, anchor="center")
        self.email_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.email_entry.place(relx=0.5, rely=0.4, anchor="center", width=250)

        # Password label and entry
        self.password_label = tk.Label(self.popup, text="Password", font=("Arial", 10))
        self.password_label.place(relx=0.4, rely=0.45, anchor="center")
        self.password_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center", width=250)

        # Notes label and entry
        self.notes_label = tk.Label(self.popup, text="Notes (optional)", font=("Arial", 10))
        self.notes_label.place(relx=0.4, rely=0.55, anchor="center")
        self.notes_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.notes_entry.place(relx=0.5, rely=0.6, anchor="center", width=250)

        # Button for saving entries in database
        self.button_save = tk.Button(self.popup, text="Save", command=self.actions.add_account_action)
        self.button_save.place(relx=0.5, rely=0.8, anchor="center")



    def open_account_window(self, account_id = None):

        self.popup = self.popup_window.create_popup(title="Account")

        # Headline
        self.add_label = tk.Label(self.popup, text="Add Account", font=("Arial", 15))
        self.add_label.place(relx=0.5, rely=0.05, anchor="center")

        # Plattform label and entry
        self.plattform_label = tk.Label(self.popup, text="Plattform", font=("Arial", 10))
        self.plattform_label.place(relx=0.4, rely=0.15, anchor="center")
        self.plattform_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.plattform_entry.place(relx=0.5, rely=0.2, anchor="center", width=250)

        # Username label and entry
        self.username_label = tk.Label(self.popup, text="Username", font=("Arial", 10))
        self.username_label.place(relx=0.4, rely=0.25, anchor="center")
        self.username_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.username_entry.place(relx=0.5, rely=0.3, anchor="center", width=250)

        # Email label and entry
        self.email_label = tk.Label(self.popup, text="Email", font=("Arial", 10))
        self.email_label.place(relx=0.4, rely=0.35, anchor="center")
        self.email_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.email_entry.place(relx=0.5, rely=0.4, anchor="center", width=250)

        # Password label and entry
        self.password_label = tk.Label(self.popup, text="Password", font=("Arial", 10))
        self.password_label.place(relx=0.4, rely=0.45, anchor="center")
        self.password_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center", width=250)

        # Notes label and entry
        self.notes_label = tk.Label(self.popup, text="Notes (optional)", font=("Arial", 10))
        self.notes_label.place(relx=0.4, rely=0.55, anchor="center")
        self.notes_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.notes_entry.place(relx=0.5, rely=0.6, anchor="center", width=250)

        # Button for saving entries in database
        self.button_save = tk.Button(self.popup, text="Save", bg="red")
        self.button_save.place(relx=0.4, rely=0.8, anchor="center")

        self.button_save = tk.Button(self.popup, text="Close",
                                     command=lambda: self.popup.destroy())
        self.button_save.place(relx=0.6, rely=0.8, anchor="center")

        if account_id is not None:
            account = database_operations.select_account(account_id)

            if account:
                self.plattform_entry.insert(0, account[1])
                self.username_entry.insert(0, account[2])
                self.email_entry.insert(0, account[3])
                self.password_entry.insert(0, account[4])
                self.notes_entry.insert(0, account[5])





    def show_screen(self, screen_name):
        controller.clear_window(self)

        if screen_name == "welcome":
            self.welcome_window()
        elif screen_name == "login":
            self.login_window()
        elif screen_name == "menu":
            self.menu_window()



