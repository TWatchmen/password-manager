import tkinter as tk
from src.backend import controller, db_logic
from src.services.actions import Actions

class MainWindow:
    def __init__(self, root, start_screen = "welcome"):
        # generate root window
        self.root = root
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)
        self.root.title("Password Manager")
        self.actions = Actions(self)
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
        self.login_label = tk.Label(self.root, text="Menu", font=("Arial", 15))
        self.login_label.place(relx=0.5, rely=0.05, anchor="center")

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        # Define Listbox
        self.listbox = tk.Listbox(self.root, width=80, height=20, font=("Arial", 12),
                                  yscrollcommand=self.scrollbar.set)
        self.listbox.place(relx=0.5, rely=0.1, anchor="n")

        # Connect scrollbar with listbox
        self.scrollbar.config(command=self.listbox.yview)

        # Button for adding new Accounts
        self.button_add = tk.Button(self.root, text="Add Account", command=self.add_account_window)
        self.button_add.place(relx=0.15, rely=0.85, anchor="s")

        # Button for changing entry
        self.button_add = tk.Button(self.root, text="Change Account")
        self.button_add.place(relx=0.3, rely=0.85, anchor="s")

        # Button for deleting entry
        self.button_add = tk.Button(self.root, text="Delete Account")
        self.button_add.place(relx=0.5, rely=0.85, anchor="s")


        # Button for settings
        self.button_settings = tk.Button(self.root, text="Settings", bg="lightgrey", fg="black",
                                         command=self.actions.settings_action)
        self.button_settings.place(relx=0.85, rely=0.85, anchor="s")

        self.actions.show_account_action()


    def add_account_window(self):
        # opening popup window
        self.popup = tk.Toplevel(self.root)
        self.popup.title("Add Account")
        self.popup.geometry("500x400")

        # Headline
        self.add_label = tk.Label(self.popup, text="Add Account", font=("Arial", 15))
        self.add_label.place(relx=0.5, rely=0.05, anchor="center")

        # Plattform label and entry
        self.plattform_label = tk.Label(self.popup, text="Plattform", font=("Arial", 10))
        self.plattform_label.place(relx=0.5, rely=0.15, anchor="center")
        self.plattform_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.plattform_entry.place(relx=0.5, rely=0.2, anchor="center")

        # Username label and entry
        self.username_label = tk.Label(self.popup, text="Username", font=("Arial", 10))
        self.username_label.place(relx=0.5, rely=0.25, anchor="center")
        self.username_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.username_entry.place(relx=0.5, rely=0.3, anchor="center")

        # Email label and entry
        self.email_label = tk.Label(self.popup, text="Email", font=("Arial", 10))
        self.email_label.place(relx=0.5, rely=0.35, anchor="center")
        self.email_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.email_entry.place(relx=0.5, rely=0.4, anchor="center")

        # Password label and entry
        self.password_label = tk.Label(self.popup, text="Password", font=("Arial", 10))
        self.password_label.place(relx=0.5, rely=0.45, anchor="center")
        self.password_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center")

        # Notes label and entry
        self.notes_label = tk.Label(self.popup, text="Notes (optional)", font=("Arial", 10))
        self.notes_label.place(relx=0.5, rely=0.55, anchor="center")
        self.notes_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.notes_entry.place(relx=0.5, rely=0.6, anchor="center")

        # Button for saving entries in database
        self.button_save = tk.Button(self.popup, text="Save", command=self.actions.add_account_action)
        self.button_save.place(relx=0.5, rely=0.8, anchor="center")


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

