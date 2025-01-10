from nicegui import ui
import sqlite3

class User:
    def __init__(self, name=None, surname=None, birthday=None, gender=None, username=None, password=None):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.gender = gender
        self.username = username
        self.password = password

    def validate_input_types(self):
        # Überprüft auf Datentypen und ob name, surname, gender nur Buchstaben enthält
        if not isinstance(self.name, str) or not self.name.isalpha():
            ui.label("Name must be a string containing only letters")
        if not isinstance(self.surname, str) or not self.surname.isalpha():
            ui.label("Surname must be a string containing only letters")
        if not isinstance(self.gender, str) or not self.gender.isalpha():
            ui.label("Gender must be a string containing only letters")
        if not isinstance(self.birthday, str):
            ui.label("Birthday must be a string (e.g., 'Date-MM-Year')")
        if not isinstance(self.username, str):
            ui.label("Username must be a string")
        if not isinstance(self.password, str):
            ui.label("Password must be a string")

        if not self.username.isalnum():  # Benutzernamen nur aus alphanumerischen Zeichen
            ui.label("Username can only contain letters and numbers")
        if len(self.password) < 6:  # Passwort muss mindestens 6 Zeichen lang sein
            ui.label("Password must be at least 6 characters long")


    def save_to_db(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute('''
        INSERT INTO users (name, surname, birthday, gender, username, password)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.name, self.surname, self.birthday, self.gender, self.username, self.password))

        connection.commit()
        connection.close()


    def get_information(self):
        with ui.card():
            ui.label("User Registartion")
            name_input = ui.input(label="Name")
            surname_input = ui.input(label="Surname")
            birthday_input = ui.input(label="Birthday")
            gender_input = ui.input(label="Gender")
            username_input = ui.input(label="Username")
            password_input = ui.input(label="Password", password=True)
            submit_input = ui.button("Submit", on_click=lambda: self.submit(name_input, surname_input, birthday_input, gender_input, username_input, password_input))
        return name_input, surname_input, birthday_input, gender_input, username_input, password_input


    def submit(self, name_input, surname_input, birthday_input, gender_input, username_input, password_input):
        user = User(
            name=name_input.value,
            surname=surname_input.value,
            birthday=birthday_input.value,
            gender=gender_input.value,
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
