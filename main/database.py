import sqlite3

def setup_database():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        birthday TEXT NOT NULL,
        gender TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS task (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        time_create DATE NOT NULL,
        time_finish DATE NOT NULL,
        priority TEXT NOT NULL,
        user_nr INTEGER,
        FOREIGN KEY (user_nr) REFERENCES users(id)
    )
    ''')

    connection.commit()
    connection.close()
