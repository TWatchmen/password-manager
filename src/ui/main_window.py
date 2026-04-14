import tkinter as tk
from operator import length_hint

# generate root window
root = tk.Tk()
root.geometry("800x600")
root.resizable(width=False, height=False)
root.title("Password Manager")


def welcome_window():
    welcome_label = tk.Label(root, text="Welcome to your Password Manager", font=("Arial", 18))
    welcome_label.place(relx=0.5, rely=0.3, anchor="center")
    label1 = tk.Label(root, text="Create your own Master Password. Don't forget your Password!", font=("Arial", 10))
    label1.place(relx=0.5, rely=0.35, anchor="center")

    master_password = tk.Entry(root, font=("Arial", 10), show="*")
    master_password.place(relx=0.5, rely=0.4, anchor="center", width=200)
    master_password_confirm = tk.Entry(root, font=("Arial", 10), show="*")
    master_password_confirm.place(relx=0.5, rely=0.45, anchor="center", width=200)


    button_register = tk.Button(root, text="Register", command=lambda: print("Register"))
    button_register.place(relx=0.5, rely=0.5, anchor="center")


    root.mainloop()


def login_window():
    login_label = tk.Label(root, text="Login", font=("Arial", 10))
    login_label.place(relx=0.5, rely=0.35, anchor="center")

    root.mainloop()

