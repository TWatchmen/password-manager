import tkinter as tk
from tkinter import font


class PopupWindow:
    def __init__(self, root):
        self.popup_height = None
        self.popup_width = None
        self.security = None
        self.password_strength_indicator_3 = None
        self.password_strength_indicator_2 = None
        self.password_strength_indicator_1 = None
        self.password_strength_label = None
        self.password_strength_indicator = None
        self.add_label = None
        self.plattform_label = None
        self.username_label = None
        self.plattform_entry = None
        self.username_entry = None
        self.email_label = None
        self.email_entry = None
        self.password_label = None
        self.password_entry = None
        self.notes_label = None
        self.notes_entry = None
        self.button_save = None
        self.root = root
        self.popup = None





    def create_popup(self, title= None):


        # opening popup window
        self.popup = tk.Toplevel(self.root)
        self.popup.title(title)
        self.popup_width = 500
        self.popup_height = 400

        # Get root window size to create popup in the middle
        self.root.update_idletasks()
        root_x = self.root.winfo_x()
        root_y = self.root.winfo_y()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()

        x = root_x + (root_width // 2) - (self.popup_width // 2)
        y = root_y + (root_height // 2) - (self.popup_height // 2)

        self.popup.geometry(f"{self.popup_width}x{self.popup_height}+{x}+{y}")
        self.popup.focus_set()



        # Headline
        tk.Label(self.popup, text="Add Account", font=("Arial", 15)).pack(expand=True)

        # Plattform label and entry
        tk.Label(self.popup, text="Plattform", font=("Arial", 10)).place(relx=0.4, rely=0.15, anchor="center")
        self.plattform_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.plattform_entry.place(relx=0.5, rely=0.2, anchor="center", width=250)

        # Username label and entry
        tk.Label(self.popup, text="Username", font=("Arial", 10)).place(relx=0.4, rely=0.25, anchor="center")
        self.username_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.username_entry.place(relx=0.5, rely=0.3, anchor="center", width=250)

        # Email label and entry
        tk.Label(self.popup, text="Email", font=("Arial", 10)).place(relx=0.4, rely=0.35, anchor="center")
        self.email_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.email_entry.place(relx=0.5, rely=0.4, anchor="center", width=250)

        # Password label and entry
        tk.Label(self.popup, text="Password", font=("Arial", 10)).place(relx=0.4, rely=0.45, anchor="center")
        self.password_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.password_entry.place(relx=0.5, rely=0.5, anchor="center", width=250)

        self.password_entry.bind("<KeyRelease>", self.security.check_password_strength)

        # Password strength indicator
        self.password_strength_indicator_1 = tk.Label(self.popup, text="   ", font=("Arial", 10))
        self.password_strength_indicator_1.place(relx=0.8, rely=0.5, anchor="center")
        self.password_strength_indicator_2 = tk.Label(self.popup, text="   ", font=("Arial", 10))
        self.password_strength_indicator_2.place(relx=0.84, rely=0.5, anchor="center")
        self.password_strength_indicator_3 = tk.Label(self.popup, text="   ", font=("Arial", 10))
        self.password_strength_indicator_3.place(relx=0.88, rely=0.5, anchor="center")

        # Notes label and entry
        tk.Label(self.popup, text="Notes (optional)", font=("Arial", 10)).place(relx=0.4, rely=0.55, anchor="center")
        self.notes_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.notes_entry.place(relx=0.5, rely=0.6, anchor="center", width=250)


        return self.popup

