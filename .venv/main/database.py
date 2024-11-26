import sqlite3

connection = sqlite3.connect("database")

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    birthday TEXT NOT NULL,
    gender TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

connection.commit()
connection.close()
print("Daten wurden erfolgreich gespeichert")