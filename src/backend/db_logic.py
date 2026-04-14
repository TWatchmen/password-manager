import sqlite3
from pathlib import Path



def create_db():
    BASE_DIR = Path(__file__).resolve().parent
    db_path = BASE_DIR.parent / "database" / "database.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)


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

create_db()
