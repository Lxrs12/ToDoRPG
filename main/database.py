import sqlite3

def setup_database():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    # Existierende `users`-Tabelle löschen, falls sie existiert
    cursor.execute('DROP TABLE IF EXISTS users')

    # Tabelle für Benutzer neu erstellen
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        race TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        profile_image TEXT,
        category TEXT NOT NULL  -- Spalte `category` hinzugefügt
    )
    ''')

    # Existierende `task`-Tabelle löschen, falls sie existiert
    cursor.execute('DROP TABLE IF EXISTS task')

    # Tabelle für Aufgaben neu erstellen
    cursor.execute('''
    CREATE TABLE task (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        time_create DATE NOT NULL,
        time_finish DATE NOT NULL,
        priority TEXT NOT NULL,
        difficulty TEXT NOT NULL,  -- Spalte `difficulty` hinzugefügt
        completed BOOLEAN DEFAULT 0,
        user_nr INTEGER,
        FOREIGN KEY (user_nr) REFERENCES users(id)
    )
    ''')

    connection.commit()
    connection.close()

# Datenbank einrichten
setup_database()
