from datetime import date
from leveling import LevelSystem  # Importiert das Levelling-System

class TaskMain:
    def __init__(self, title, description, time_finish, priority):
        self.title = title
        self.description = description
        self.time_create = date.today()  # Erstellungsdatum wird automatisch gesetzt
        self.time_finish = time_finish  # Enddatum wird übergeben
        self.priority = priority  # Priorität wird übergeben
        self.completed = False  # Status der Aufgabe

class TaskManager:
    def __init__(self):
        self.tasks = []  # Eine Liste zum Speichern der Tasks
        self.level_system = LevelSystem()  # Erstelle ein Level-System-Objekt

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' hinzugefügt.")  # Ausgabe des Titels

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title and not task.completed:
                task.completed = True
                print(f"Task '{task.title}' wurde abgeschlossen.")
                self.level_system.complete_task()
                return
        print(f"Task '{title}' nicht gefunden oder bereits abgeschlossen.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{task.title}' wurde gelöscht.")
                return
        print(f"Task '{title}' nicht gefunden.")

    def __str__(self):
        return str(self.level_system)

# Funktion zum Erfassen der Aufgabendetails vom Benutzer
def get_task_details():
    title = input("Titel der Aufgabe: ")
    description = input("Beschreibung der Aufgabe: ")
    year = int(input("Enddatum - Jahr: "))
    month = int(input("Enddatum - Monat: "))
    day = int(input("Enddatum - Tag: "))
    time_finish = date(year, month, day)
    priority = input("Priorität der Aufgabe (low, medium, high): ")
    return TaskMain(title, description, time_finish, priority)

# Erstellen einer Instanz von TaskManager
task_manager = TaskManager()

# Benutzer nach Aufgabeninformationen fragen
print("Bitte geben Sie die Details der Aufgabe ein.")
task = get_task_details()
task_manager.add_task(task)

title_to_complete = input("Titel der abzuschließenden Aufgabe: ")
task_manager.complete_task(title_to_complete)

title_to_remove = input("Titel der zu löschenden Aufgabe: ")
task_manager.remove_task(title_to_remove)

print(task_manager)
