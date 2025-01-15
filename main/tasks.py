import sqlite3
from datetime import date
from nicegui import ui
from leveling import LevelSystem

# Datenbank und Tabelle erstellen
def create_database():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS task')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS task (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        time_create TEXT,
        time_finish TEXT,
        priority TEXT,
        difficulty TEXT,
        completed INTEGER DEFAULT 0,
        user_nr INTEGER
    )
    ''')
    connection.commit()
    connection.close()
    ui.notify("Neue Datenbank und Tabelle 'task' wurden erstellt.")
create_database()

# Aufgabenklasse
class TaskMain:
    def __init__(self, title, description, time_finish, priority, difficulty):
        self.title = title
        self.description = description
        self.time_create = date.today()  # Automatisch gesetztes Erstellungsdatum
        self.time_finish = time_finish  # Übergebenes Enddatum
        self.priority = priority  # Übergebene Priorität
        self.difficulty = difficulty  # Übergebener Schwierigkeitsgrad
        self.completed = False  # Aufgabenstatus

    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Created: {self.time_create}, Finish: {self.time_finish}, Priority: {self.priority}, Difficulty: {self.difficulty}, Completed: {self.completed}"

# Aufgabenverwaltung
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.level_system = LevelSystem()
        self.load_tasks_from_database()

    def load_tasks_from_database(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute('SELECT title, description, time_create, time_finish, priority, difficulty, completed FROM task')
        rows = cursor.fetchall()
        for row in rows:
            task = TaskMain(row[0], row[1], date.fromisoformat(row[3]), row[4], row[5])
            task.completed = bool(row[6])
            self.tasks.append(task)
        connection.close()

    def add_task(self, task):
        self.tasks.append(task)
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO task (title, description, time_create, time_finish, priority, difficulty, user_nr)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            task.title, task.description, task.time_create.isoformat(), task.time_finish.isoformat(), task.priority,
            task.difficulty, None))
        connection.commit()
        connection.close()
        ui.notify(f"Task '{task.title}' wurde hinzugefügt.")

    def complete_task(self, title):
        task_found = False
        for task in self.tasks:
            if task.title == title and not task.completed:
                task.completed = True
                task_found = True
                self.level_system.complete_task(task.difficulty)
                connection = sqlite3.connect("database.db")
                cursor = connection.cursor()
                cursor.execute('UPDATE task SET completed = 1 WHERE title = ?', (title,))
                connection.commit()
                connection.close()
                ui.notify(f"Task '{title}' wurde abgeschlossen.")
                display_level_status()
                break
        if not task_found:
            ui.notify(f"Task '{title}' nicht gefunden oder bereits abgeschlossen.")

    def remove_task(self, title):
        task_found = False
        for task in self.tasks:
            if task.title == title:
                task_found = True
                self.tasks.remove(task)
                connection = sqlite3.connect("database.db")
                cursor = connection.cursor()
                cursor.execute('DELETE FROM task WHERE title = ?', (title,))
                connection.commit()
                connection.close()
                ui.notify(f"Task '{title}' wurde gelöscht.")
                break
        if not task_found:
            ui.notify(f"Task '{title}' nicht gefunden.")

task_manager = TaskManager()

# Aktionen für die Benutzeroberfläche definieren
def add_task_action():
    if not (title.value and description.value and year.value and month.value and day.value and priority.value and difficulty.value):
        ui.notify("Bitte füllen Sie alle Felder aus.")
        return
    task = TaskMain(title.value, description.value, date(int(year.value), int(month.value), int(day.value)),
                    priority.value, difficulty.value)
    task_manager.add_task(task)

def complete_task_action():
    task_manager.complete_task(title_to_complete.value)

def remove_task_action():
    task_manager.remove_task(title_to_remove.value)

def display_tasks_action():
    task_list.clear()
    with task_list:
        for task in task_manager.tasks:
            if not task.completed:
                ui.label(str(task)).classes('mb-3')

def display_level_status():
    level_info.clear()
    with level_info:
        ui.label(f"Aktuelles Level: {task_manager.level_system.level}")
        ui.label(f"Erfahrungspunkte: {task_manager.level_system.points}/{task_manager.level_system.points_for_next_level}")
        ui.label(f"Noch {task_manager.level_system.points_for_next_level - task_manager.level_system.points} Punkte bis zum nächsten Level")
    ui.label(f"Abzeichen: {', '.join(task_manager.level_system.badges)}")

# Benutzeroberfläche erstellen
with ui.column().classes('items-center'):
    ui.label('Neue Aufgabe hinzufügen').classes('text-h4')
    title = ui.input('Titel der Aufgabe').classes('w-full')
    description = ui.input('Beschreibung der Aufgabe').classes('w-full')
    year = ui.input('Enddatum - Jahr').classes('w-full')
    month = ui.input('Enddatum - Monat').classes('w-full')
    day = ui.input('Enddatum - Tag').classes('w-full')
    priority = ui.select(['low', 'medium', 'high'], label='Priorität der Aufgabe').classes('w-full')
    difficulty = ui.select(['easy', 'medium', 'difficult'], label='Schwierigkeitsgrad der Aufgabe').classes('w-full')
    ui.button('Aufgabe hinzufügen', on_click=add_task_action).classes('w-full')

    ui.separator().classes('my-4')
    ui.label('Aufgabe abschließen').classes('text-h4')
    title_to_complete = ui.input('Titel der abzuschließenden Aufgabe').classes('w-full')
    ui.button('Aufgabe abschließen', on_click=complete_task_action).classes('w-full')

    ui.separator().classes('my-4')
    ui.label('Aufgabe löschen').classes('text-h4')
    title_to_remove = ui.input('Titel der zu löschenden Aufgabe').classes('w-full')
    ui.button('Aufgabe löschen', on_click=remove_task_action).classes('w-full')

    ui.separator().classes('my-4')
    ui.label('Aufgabenliste').classes('text-h4')
    task_list = ui.column().classes('w-full')
    ui.button('Aufgabenliste anzeigen', on_click=display_tasks_action).classes('w-full')

    ui.separator().classes('my-4')
    ui.label('Level-Status').classes('text-h4')
    level_info = ui.column().classes('w-full')

ui.run()