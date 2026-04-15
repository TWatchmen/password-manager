import tkinter as tk

from src.backend import password_manager



class MainWindow:
    def __init__(self, root, start_screen = "welcome"):
        # generate root window
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

    def login_window(self):
        self.login_label = tk.Label(self.root, text="Login", font=("Arial", 15))
        self.login_label.place(relx=0.5, rely=0.35, anchor="center")

        self.master_password = tk.Entry(self.root, font=("Arial", 10), show="*")
        self.master_password.place(relx=0.5, rely=0.4, anchor="center", width=200)

        self.button_register = tk.Button(self.root, text="Login", command=self.login_action)
        self.button_register.place(relx=0.5, rely=0.5, anchor="center")

    def menu_window(self):
        self.login_label = tk.Label(self.root, text="Menu", font=("Arial", 15))
        self.login_label.place(relx=0.5, rely=0.35, anchor="center")





    def login_action(self):
        pwd = self.master_password.get().strip()
        password_manager.login(pwd)
        password_manager.login(pwd)

        success = password_manager.login(pwd)
        if success:
            self.show_screen("menu")


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

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

