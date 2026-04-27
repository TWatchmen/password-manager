from pathlib import Path
import tkinter as tk
from src.ui.main_window import MainWindow
from src.config import DB_PATH

"""

Master Password: 123

"""


# Starting the GUI
root = tk.Tk()

# Checking if database path already exits
if DB_PATH.exists():
    app = MainWindow(root, start_screen="login", main_ui=True, popup_ui=True)
else:
    app = MainWindow(root, start_screen="welcome", main_ui=True, popup_ui=True)

# Run
root.mainloop()





