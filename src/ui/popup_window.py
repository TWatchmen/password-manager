import tkinter as tk

from src.ui import main_window


class PopupWindow:
    def __init__(self, root):
        self.root = root
        self.popup = None



    def create_popup(self, title= None):
        # opening popup window
        self.popup = tk.Toplevel(self.root)
        self.popup.title(title)
        self.popup.geometry("500x400")
        return self.popup


