from datetime import date
from leveling import LevelSystem  # Importiert das Levelling-System

# Hauptklasse zur Darstellung einer Aufgabe
class TaskMain:
    def __init__(self, title, description, time_finish, priority):
        self.title = title
        self.description = description
        self.time_create = date.today()  # Erstellungsdatum wird automatisch gesetzt
        self.time_finish = time_finish  # Enddatum wird übergeben
        self.priority = priority  # Priorität wird übergeben
        self.completed = False  # Status der Aufgabe

    # Darstellung der Aufgabe als String
    def __str__(self):
        return f"Title: {self.title}, Description: {self.description}, Created: {self.time_create}, Finish: {self.time_finish}, Priority: {self.priority}, Completed: {self.completed}"

# Klasse zur Verwaltung von Aufgaben
class TaskManager:
    def __init__(self):
        self.tasks = []  # Eine Liste zum Speichern der Tasks
        self.level_system = LevelSystem()  # Erstelle ein Level-System-Objekt

    # Funktion zum Hinzufügen einer Aufgabe
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' hinzugefügt.")  # Ausgabe des Titels

    # Funktion zum Abschließen einer Aufgabe
    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title and not task.completed:
                task.completed = True
                print(f"Task '{task.title}' wurde abgeschlossen.")
                self.level_system.complete_task()
                return
        print(f"Task '{title}' nicht gefunden oder bereits abgeschlossen.")

    # Funktion zum Entfernen einer Aufgabe
    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{task.title}' wurde gelöscht.")
                return
        print(f"Task '{title}' nicht gefunden.")

    # Darstellung der Aufgabenliste und Level-System als String
    def __str__(self):
        task_str = "\n".join([str(task) for task in self.tasks])
        return f"Tasks:\n{task_str}\nLevel System:\n{self.level_system}"

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

# Benutzer nach abzuschließender Aufgabe fragen
title_to_complete = input("Titel der abzuschließenden Aufgabe: ")
task_manager.complete_task(title_to_complete)

# Benutzer nach zu löschender Aufgabe fragen
title_to_remove = input("Titel der zu löschenden Aufgabe: ")
task_manager.remove_task(title_to_remove)

# Ausgabe des TaskManagers
print(task_manager)
