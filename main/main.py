import database
from user import User
from tasks import TaskManager, create_ui
from nicegui import ui

# Datenbank einrichten
database.setup_database()

# Initialisierung der Aufgabenverwaltung
task_manager = TaskManager()

# Benutzeroberfläche für Benutzerregistrierung
user = User()
user.get_information()


# Benutzeroberfläche für Aufgabenverwaltung
@ui.page('/tasks')
def tasks_page():
    create_ui()

ui.run()

