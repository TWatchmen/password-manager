import sqlite3
from src.utils.config import DB_PATH as db_path
from src.models.account import Account


"""
    All database accesses are written in this file.
    # create_db() creates the database and is executed only when the file is first opened.
    # insert_master_pwd 
"""


db_path.parent.mkdir(parents=True, exist_ok=True)

def create_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS master
                    (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        password TEXT NOT NULL
                    )
                    """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS accounts
                   (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       plattform TEXT NOT NULL,
                       username Text,
                       email Text NOT NULL,
                       password TEXT NOT NULL,
                       notes TEXT
                   )
                   """)
    conn.commit()
    conn.close()

def insert_master_pwd(password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO master 
                          (password)
                      VALUES (?)
        """,
        (password,)
    )
    conn.commit()
    conn.close()

def insert_account(plattform, username, email, password, notes):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO accounts 
               (plattform, 
                username, 
                email, 
                password, 
                notes) 
           VALUES (?, ?, ?, ?, ?)
        """,
        (plattform, username, email, password, notes, )
    )
    conn.commit()
    conn.close()

def check_login(password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""SELECT password 
                      FROM master 
                      WHERE id = 1
                   """)
    result = cursor.fetchone()
    conn.close()

    stored_password = result[0]
    if stored_password == password:
        return password
    return None

def show_accounts():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM accounts 
                      ORDER BY plattform ASC
                   """)
    rows = cursor.fetchall()
    conn.close()
    return [Account.from_db_row(row) for row in rows]

def select_account(account_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM accounts 
                      WHERE id = ?
                   """, (account_id,))
    row = cursor.fetchone()
    conn.close()
    return Account.from_db_row(row)

def save_account(account_id, plattform, username, email, password, notes):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """UPDATE accounts
           SET plattform=?,
               username=?,
               email=?,
               password=?,
               notes=?
           WHERE id = ?""",
        (plattform, username, email, password, notes, account_id)
    )
    conn.commit()
    conn.close()

def save_master(password, master_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        """ UPDATE master
            SET password=?
            WHERE id=?""",
        (password, master_id)
    )
    conn.commit()
    conn.close()
