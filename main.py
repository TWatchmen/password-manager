from pathlib import Path
from src.ui.main_window import *

"""

Master Password: 123

"""

# Getting database path
BASE_DIR = Path(__file__).resolve().parent
database_file_path = BASE_DIR / "src/database/database.db"

# Starting the GUI
root = tk.Tk()

# Checking if database path already exits
if database_file_path.exists():
    app = MainWindow(root, start_screen="login")
else:
    app = MainWindow(root, start_screen="welcome")

# Run
root.mainloop()





