from nicegui import ui
import sqlite3

class User:
    def __init__(self, race=None, username=None, password=None, category=None):
        self.race = race
        self.username = username
        self.password = password
        self.category = category

    def validate_input_types(self):
        if not isinstance(self.username, str):
            ui.notify("Username must be a string")
            return False

        if not isinstance(self.password, str):
            ui.notify("Password must be a string")
            return False

        if len(self.password) < 6:
            ui.notify("Password must be at least 6 characters long")
            return False

        return True

    def check_unique_username(self, username):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute('SELECT COUNT(*) FROM users WHERE username = ?', (username,))
        count = cursor.fetchone()[0]
        connection.close()
        return count == 0

    def save_to_db(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        try:
            cursor.execute('''
            INSERT INTO users (race, username, password, category) 
            VALUES (?, ?, ?, ?)
            ''', (self.race, self.username, self.password, self.category))
            connection.commit()
        except sqlite3.IntegrityError:
            ui.notify("Username already exists. Please choose a different username.")
        finally:
            connection.close()

    def get_information(self):
        with ui.card():
            ui.label("User Registration")
            race_input = ui.select(
                label="Race",
                options=["Human", "Elve", "Orc", "Gnome", "Undead"],
                on_change=lambda: self.update_profile_img(race_input.value)
            )

            category_input = ui.select(
                label="Class",
                options=["Knight", "Barbar", "Priest", "Rogue", "Mage"]
            )
            username_input = ui.input(label="Username")
            password_input = ui.input(label="Password", password=True)
            ui.button("Submit", on_click=lambda: self.submit(race_input.value, username_input.value, password_input.value, category_input.value))
            self.update_profile_img(race_input.value)

    def update_profile_img(self, race):
        if race == "Human":
            ui.image("media/Mensch.png")
        elif race == "Elve":
            ui.image("media/Elve.png")
        elif race == "Orc":
            ui.image("media/org.png")
        elif race == "Gnome":
            ui.image("media/gnom.png")
        elif race == "Undead":
            ui.image("media/untot.png")

    def submit(self, race, username, password, category):
        self.race = race
        self.username = username
        self.password = password
        self.category = category

        if self.validate_input_types():
            if self.check_unique_username(username):
                self.save_to_db()
                ui.notify("User was saved successfully")
                ui.link("Go to Tasks", "/tasks")  # Routenwechsel zu Tasks nach erfolgreicher Registrierung
            else:
                ui.notify("Username already exists. Please choose a different username.")


