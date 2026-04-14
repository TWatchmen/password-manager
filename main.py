from pathlib import Path
from src.ui.main_window import *

BASE_DIR = Path(__file__).resolve().parent
database_file_path = BASE_DIR / "src/database/database.db"




if not database_file_path.exists():
    main_window = welcome_window()
    if __name__ == "__main":
        main_window.show()
else:
    main_window = login_window()
    if __name__ == "__main__":
        main_window.show()





