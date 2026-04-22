import tkinter as tk

from src.backend import password_manager


class MainWindow:
    def __init__(self, root, start_screen = "welcome"):
        # generate root window
        self.password_label = None
        self.notes_label = None
        self.email_label = None
        self.username_label = None
        self.plattform_label = None
        self.button_login = None
        self.add_label = None
        self.username = None
        self.notes = None
        self.password = None
        self.plattform = None
        self.email = None
        self.button_save = None
        self.popup = None
        self.button_settings = None
        self.button_add = None
        self.listbox = None
        self.scrollbar = None
        self.table_frame = None
        self.button_register = None
        self.login_label = None
        self.root = root
        self.root.geometry("800x600")
        self.root.resizable(width=False, height=False)
        self.root.title("Password Manager")
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


        self.button_register = tk.Button(self.root, text="Register", command=self.register_action)
        self.button_register.place(relx=0.5, rely=0.5, anchor="center")

    # Login user interface
    def login_window(self):
        self.login_label = tk.Label(self.root, text="Login", font=("Arial", 15))
        self.login_label.place(relx=0.5, rely=0.35, anchor="center")

        self.master_password = tk.Entry(self.root, font=("Arial", 10), show="*")
        self.master_password.place(relx=0.5, rely=0.4, anchor="center", width=200)

        self.button_login = tk.Button(self.root, text="Login", command=self.login_action)
        self.button_login.place(relx=0.5, rely=0.5, anchor="center")

    # Menu user interface
    def menu_window(self):
        self.login_label = tk.Label(self.root, text="Menu", font=("Arial", 15))
        self.login_label.place(relx=0.5, rely=0.05, anchor="center")

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        # Define Listbox
        self.listbox = tk.Listbox(self.root, width=100, height=25, yscrollcommand=self.scrollbar.set)
        self.listbox.place(relx=0.5, rely=0.1, anchor="n")

        # Connect scrollbar with listbox
        self.scrollbar.config(command=self.listbox.yview)

        # Button for adding new Accounts
        self.button_add = tk.Button(self.root, text="Add Account", command=self.add_account_action)
        self.button_add.place(relx=0.15, rely=0.85, anchor="s")


        # Button for settings
        self.button_settings = tk.Button(self.root, text="Settings", bg="lightgrey", fg="black",
                                         command=self.settings_action)
        self.button_settings.place(relx=0.85, rely=0.85, anchor="s")

    # Function login action for button
    def login_action(self):
        pwd = self.master_password.get().strip()
        success = password_manager.login(pwd)
        if success:
            self.show_screen("menu")


    # Function adding action to the button
    def add_account_action(self):
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
        self.plattform = tk.Entry(self.popup, font=("Arial", 10))
        self.plattform.place(relx=0.5, rely=0.2, anchor="center")

        # Username label and entry
        self.username_label = tk.Label(self.popup, text="Username", font=("Arial", 10))
        self.username_label.place(relx=0.5, rely=0.25, anchor="center")
        self.username = tk.Entry(self.popup, font=("Arial", 10))
        self.username.place(relx=0.5, rely=0.3, anchor="center")

        # Email label and entry
        self.email_label = tk.Label(self.popup, text="Email", font=("Arial", 10))
        self.email_label.place(relx=0.5, rely=0.35, anchor="center")
        self.email = tk.Entry(self.popup, font=("Arial", 10))
        self.email.place(relx=0.5, rely=0.4, anchor="center")

        # Password label and entry
        self.password_label = tk.Label(self.popup, text="Password", font=("Arial", 10))
        self.password_label.place(relx=0.5, rely=0.45, anchor="center")
        self.password = tk.Entry(self.popup, font=("Arial", 10))
        self.password.place(relx=0.5, rely=0.5, anchor="center")

        # Notes label and entry
        self.notes_label = tk.Label(self.popup, text="Notes", font=("Arial", 10))
        self.notes_label.place(relx=0.5, rely=0.55, anchor="center")
        self.notes = tk.Entry(self.popup, font=("Arial", 10))
        self.notes.place(relx=0.5, rely=0.6, anchor="center")



        self.button_save = tk.Button(self.popup,text="Save")
        self.button_save.place(relx=0.5, rely=0.8, anchor="center")





    def settings_action(self):
        return

    def register_action(self):
        pwd = self.master_password.get().strip()
        confirm_pwd = self.master_password_confirm.get().strip()
        password_manager.register(pwd, confirm_pwd)

        success = password_manager.register(pwd, confirm_pwd)
        if success:
            self.show_screen("login")


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

