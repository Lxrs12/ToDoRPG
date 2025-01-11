from nicegui import ui
import sqlite3

class User:
    def __init__(self, race=None, username=None, password=None):
        self.race = race
        self.username = username
        self.password = password

    def validate_input_types(self):
# Function to validate the inputs

        if not isinstance(self.username, str):
            ui.label("Username must be a string")

        if not isinstance(self.password, str):
            ui.label("Password must be a string")

        if len(self.password) < 6:
            ui.label("Password must be at least 6 characters long")


    def save_to_db(self):
# Function that saves the User to the Database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute('''
        INSERT INTO users (race, username, password)
        VALUES (?, ?, ?)
        ''', (self.race, self.username, self.password))

        connection.commit()
        connection.close()


    def get_information(self):
# Function that creates a gui and makes it able to give the User inputs
        with ui.card():
            ui.label("User Registartion")
            race_input = ui.select(
                label="Race",
                options = ["Human", "Elve", "Orc", "Gnome", "Undead"],
                on_change=lambda: self.update_profile_img(race_input.value)
            )
            username_input = ui.input(label="Username")
            password_input = ui.input(label="Password", password=True)
            submit_input = ui.button("Submit", on_click=lambda: self.submit(race_input, username_input, password_input))
            self.update_profile_img(race_input.value)
        return race_input, username_input, password_input

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


    def submit(self, race_input, username_input, password_input):
# This Function is about the Button so that the user can be saved
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
race_input, username_input, password_input= user.get_information()
ui.run()