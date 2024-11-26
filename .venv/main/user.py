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
            raise ValueError("Name must be a string containing only letters")
        if not isinstance(self.surname, str) or not self.surname.isalpha():
            raise ValueError("Surname must be a string containing only letters")
        if not isinstance(self.gender, str) or not self.gender.isalpha():
            raise ValueError("Gender must be a string containing only letters")
        if not isinstance(self.birthday, str):
            raise ValueError("Birthday must be a string (e.g., 'Date-MM-Year')")
        if not isinstance(self.username, str):
            raise ValueError("Username must be a string")
        if not isinstance(self.password, str):
            raise ValueError("Password must be a string")

        if not self.username.isalnum():  # Benutzernamen nur aus alphanumerischen Zeichen
            raise ValueError("Username can only contain letters and numbers")
        if len(self.password) < 6:  # Passwort muss mindestens 6 Zeichen lang sein
            raise ValueError("Password must be at least 6 characters long")

    def get_informations(self):
        self.name = input("Enter your Name: ")
        self.surname = input("Enter your Surname: ")
        self.birthday = input("Enter your Birthday: ")
        self.gender = input("Enter your Gender: ")
        self.username = input("Enter your Username: ")
        self.password = input("Enter your Password: ")

        self.validate_input_types()

    def create_user(self):
        self.get_informations()
        return self

    def save_to_db(self):
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute('''
        INSERT INTO users (name, surname, birthday, gender, username, password)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.name, self.surname, self.birthday, self.gender, self.username, self.password))

        connection.commit()
        connection.close()
        print("User was saved")

    def __str__(self):
        return f"User(name={self.name}, surname={self.surname}, birthday={self.birthday}, gender={self.gender}, username={self.username}, password={self.password})"

user = User().create_user()
print(user)
