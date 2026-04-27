import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
db_path = BASE_DIR.parent / "data" / "database.db"
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
                   CREATE TABLE IF NOT EXISTS accounts
                   (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       plattform TEXT NOT NULL,
                       username Text,
                       email Text NOT NULL,
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

def insert_account(plattform, username, email, password, notes):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO accounts (plattform, username, email, password, notes) VALUES (?, ?, ?, ?, ?)",
        (plattform, username, email, password, notes, )
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

def show_accounts():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts ORDER BY plattform ASC")
    result = cursor.fetchall()
    conn.close()
    return result

def select_account(account_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE id = ?", (account_id,))
    result = cursor.fetchone()
    conn.close()
    return result
