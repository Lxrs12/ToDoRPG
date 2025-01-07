class LevelSystem:
    def __init__(self):
        self.level = 1
        self.completed_task_count = 0
        self.tasks_for_next_level = 3  # Anzahl Aufgaben zum nächsten Level

    def complete_task(self):
        self.completed_task_count += 1
        self.check_level_up()

    def check_level_up(self):
        while self.completed_task_count >= self.tasks_for_next_level:
            self.completed_task_count -= self.tasks_for_next_level
            self.level_up()

    def level_up(self):
        self.level += 1
        self.tasks_for_next_level = int(self.tasks_for_next_level * 1.2)  # Anzahl der benötigten Aufgaben steigt mit jedem Level
        print(f"Herzlichen Glückwunsch, du hast Level {self.level} erreicht!")

    def __str__(self):
        return f"Level: {self.level}, Abgeschlossene Aufgaben: {self.completed_task_count}/{self.tasks_for_next_level}"
