import database
from user import User
from tasks import TaskManager, create_ui
from nicegui import ui

# Datenbank einrichten
database.setup_database()

# Initialisierung der Aufgabenverwaltung
task_manager = TaskManager()

# Benutzeroberfläche für Benutzerregistrierung
@ui.page('/register')
def register_page():
    user = User()
    user.get_information()

@ui.page('/login')
def login_page():
    user = User()
    user.login_page()

# Benutzeroberfläche für Aufgabenverwaltung
@ui.page('/tasks')
def tasks_page():
    create_ui()

ui.run()

