from pathlib import Path
from src.ui.main_window import *

"""

Master Password: 123

"""


BASE_DIR = Path(__file__).resolve().parent
database_file_path = BASE_DIR / "src/database/database.db"

root = tk.Tk()

if database_file_path.exists():
    app = MainWindow(root, start_screen="login")
else:
    app = MainWindow(root, start_screen="welcome")

root.mainloop()





