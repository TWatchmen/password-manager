import tkinter as tk


class PopupWindow:
    def __init__(self, root):
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
        self.popup.geometry("500x400")

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
        self.password_entry.bind("<KeyRelease>", self.check_password_strength)
        self.password_strength_label = tk.Label(self.popup, text="Password Strength", font=("Arial", 8))
        self.password_strength_label.place(relx=0.8, rely=0.45, anchor="center")
        self.password_strength_indicator = tk.Label(self.popup, text="     ", font=("Arial", 10), bg="red")
        self.password_strength_indicator.place(relx=0.8, rely=0.5, anchor="center")

        # Notes label and entry
        self.notes_label = tk.Label(self.popup, text="Notes (optional)", font=("Arial", 10))
        self.notes_label.place(relx=0.4, rely=0.55, anchor="center")
        self.notes_entry = tk.Entry(self.popup, font=("Arial", 10))
        self.notes_entry.place(relx=0.5, rely=0.6, anchor="center", width=250)


        return self.popup


    def check_password_strength(self, event=None):
        password = self.password_entry.get()

        if len(password) >= 8:
            self.password_strength_indicator.config(bg="green")
        else:
            self.password_strength_indicator.config(bg="red")


