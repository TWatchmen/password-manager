import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
db_path = BASE_DIR.parent / "database" / "database.db"
db_path.parent.mkdir(parents=True, exist_ok=True)

def create_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS master
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        password TEXT NOT NULL
                    )
                    ''')

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS passwords
                   (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       plattform TEXT NOT NULL,
                       username Text,
                       mail Text NOT NULL,
                       password TEXT NOT NULL,
                       notes TEXT
                   )
                   ''')

    conn.commit()
    conn.close()


def insert_master_pwd(password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO master (password) VALUES (?)",
        (password,)
    )
    conn.commit()
    conn.close()

def check_login(password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM master WHERE id = 1")
    result = cursor.fetchone()
    conn.close()

    stored_password = result[0]
    if stored_password == password:
        return password
    return None

