class LevelSystem:
    def __init__(self):
        self.level = 1
        self.points = 0  # Gesammelte Punkte
        self.points_for_next_level = 20  # Punkte zum nächsten Level
        self.badges = []  # Hinzugefügte Abzeichen

    def complete_task(self, difficulty):
        self.add_points(difficulty)
        self.check_level_up()

    def add_points(self, difficulty):
        if difficulty == "easy":
            self.points += 2
        elif difficulty == "medium":
            self.points += 5
        elif difficulty == "difficult":
            self.points += 10

    def check_level_up(self):
        while self.points >= self.points_for_next_level:
            self.points -= self.points_for_next_level
            self.level_up()

    def level_up(self):
        self.level += 1
        self.check_badges()  # Überprüfen, ob ein Abzeichen verdient wurde
        self.points_for_next_level = int(self.points_for_next_level * 1.2)  # Erfahrungspunkte-Anforderung steigt mit jedem Level
        print(f"Herzlichen Glückwunsch, du hast Level {self.level} erreicht!")

    def check_badges(self):
        if self.level == 5:
            self.badges.append("Bronze-Abzeichen")
            print("Du hast das Bronze-Abzeichen erhalten!")
        elif self.level == 10:
            self.badges.append("Silber-Abzeichen")
            print("Du hast das Silber-Abzeichen erhalten!")
        elif self.level == 20:
            self.badges.append("Gold-Abzeichen")
            print("Du hast das Gold-Abzeichen erhalten!")

    def __str__(self):
        remaining_points = self.points_for_next_level - self.points
        return (f"Level: {self.level}, Erfahrungspunkte: {self.points}/{self.points_for_next_level}, "
                f"Noch {remaining_points} Punkte bis zum nächsten Level, Abzeichen: {', '.join(self.badges)}")
