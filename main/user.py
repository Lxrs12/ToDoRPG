from nicegui import ui
import sqlite3

class User:
    def __init__(self, race=None, username=None, password=None):
        self.race = race
        self.username = username
        self.password = password

    def validate_input_types(self):
        valid = True

        if not isinstance(self.username, str):
            ui.label("Username must be a string")
            valid = False
        if not isinstance(self.password, str):
            ui.label("Password must be a string")
            valid = False
        if len(self.password) < 6:  # Passwort muss mindestens 6 Zeichen lang sein
            ui.label("Password must be at least 6 characters long")
            valid = False


    def save_to_db(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute('''
        INSERT INTO users (race, username, password)
        VALUES (?, ?, ?)
        ''', (self.race, self.username, self.password))

        connection.commit()
        connection.close()


    def get_information(self):
        with ui.card():
            ui.label("User Registartion")
            race_input = ui.select(
                label="race",
                options = ["Human", "Elve", "Orc", "Gnome", "Undead"]
            )
            username_input = ui.input(label="Username")
            password_input = ui.input(label="Password", password=True)
            submit_input = ui.button("Submit", on_click=lambda: self.submit(race_input, username_input, password_input))
        return race_input, username_input, password_input


    def submit(self, race_input, username_input, password_input):
        user = User(
            race=race_input.value,
            username=username_input.value,
            password=password_input.value
        )

        try:
            user.validate_input_types()
            user.save_to_db()
            ui.label("User was saved Succesfully")

        except:
            ui.label("User can not be saved in the Database")


user = User()
user.get_information()
ui.run()

