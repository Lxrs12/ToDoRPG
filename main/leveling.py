class LevelSystem:
    def __init__(self):
        self.level = 1
        self.points = 0  # Gesammelte Punkte
        self.points_for_next_level = 20  # Punkte zum nächsten Level
        self.badges = []  # Hinzugefügte Abzeichen
        self.difficulty_points = {"easy": 2, "medium": 5, "difficult": 10}  # Punktwerte für Schwierigkeitsgrade

    def complete_task(self, difficulty):
        self.add_points(difficulty)
        self.check_level_up()

    def add_points(self, difficulty):
        if difficulty in self.difficulty_points:
            self.points += self.difficulty_points[difficulty]

    def set_difficulty_points(self, difficulty, points):
        if difficulty in self.difficulty_points:
            self.difficulty_points[difficulty] = points

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
        badges_dict = {5: "Bronze-Abzeichen", 10: "Silber-Abzeichen", 20: "Gold-Abzeichen"}
        if self.level in badges_dict:
            self.badges.append(badges_dict[self.level])
            print(f"Du hast das {badges_dict[self.level]} erhalten!")

    def __str__(self):
        remaining_points = self.points_for_next_level - self.points
        return (f"Level: {self.level}, Erfahrungspunkte: {self.points}/{self.points_for_next_level}, "
                f"Noch {remaining_points} Punkte bis zum nächsten Level, Abzeichen: {', '.join(self.badges)}")