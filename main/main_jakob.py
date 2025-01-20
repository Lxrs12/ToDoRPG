import database
from tasks import TaskManager, create_ui
from nicegui import ui

# Datenbank erstellen
database.setup_database()

# Initialisieren der Aufgabenverwaltung
task_manager = TaskManager()

# Benutzeroberfläche für Aufgabenverwaltung
@ui.page('/tasks')
def tasks_page():
    create_ui()

ui.run()
tasks_page()