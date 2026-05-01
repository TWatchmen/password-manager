import string
import random
import tkinter as tk
from tkinter.constants import INSERT

import bcrypt


class PasswordSecurity:
    def __init__(self, popup_ui):
        self.popup_window = popup_ui
        self.popup_ui = popup_ui
        return

    def check_password_strength(self, event=None):
        password = self.popup_window.password_entry.get()

        # Label "Password Strength"
        (tk.Label(self.popup_window.popup, text="Password Strength", font=("Arial", 8))
         .place(relx=0.85, rely=0.45, anchor="center"))

        self.popup_window.password_strength_indicator_1.configure(bg="lightgrey")
        self.popup_window.password_strength_indicator_2.configure(bg="lightgrey")
        self.popup_window.password_strength_indicator_3.configure(bg="lightgrey")

        length = len(password)

        if length >= 5:
            self.popup_window.password_strength_indicator_1.config(bg="red")

        if length >= 5 and (password.isalpha() is False or password.isalnum() is False):
            self.popup_window.password_strength_indicator_1.config(bg="red")
            self.popup_window.password_strength_indicator_2.config(bg="yellow")

        if length >= 5 and password.isalnum() is False and password.isalpha() is False:
            self.popup_window.password_strength_indicator_1.config(bg="yellow")
            self.popup_window.password_strength_indicator_2.config(bg="yellow")
            self.popup_window.password_strength_indicator_3.config(bg="yellow")

        if length >= 8:
            self.popup_window.password_strength_indicator_2.config(bg="yellow")

        if length >= 8 and password.isalpha() is False:
            self.popup_window.password_strength_indicator_3.config(bg="green")

        if length >= 8 and password.isalpha() is False and password.isalnum() is False:
            self.popup_window.password_strength_indicator_1.config(bg="green")
            self.popup_window.password_strength_indicator_2.config(bg="green")
            self.popup_window.password_strength_indicator_3.config(bg="green")



    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        random_password = "".join(random.choice(characters) for _ in range(12))

        self.popup_ui.password_entry.delete(0, tk.END)
        self.popup_ui.password_entry.insert(INSERT, random_password)
        self.popup_ui.security.check_password_strength()



class DatabaseSecurity:
    def __init__(self):
        return


    @staticmethod
    def hash_password(password:str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    @staticmethod
    def verify_password(password:str, hashed_password:str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


