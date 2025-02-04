from nicegui import ui
import sqlite3


class User:
    def __init__(self, race=None, username=None, password=None, category=None):
        self.race = race
        self.username = username
        self.password = password
        self.category = category

    def validate_input_types(self):
# Function to validate the inputs

        if not isinstance(self.username, str):
            ui.label("Username must be a string")
                                                    # Überflüssig
        if not isinstance(self.password, str):
            ui.label("Password must be a string")

        if len(self.password) < 6:
            ui.label("Password must be at least 6 characters long")


    def save_to_db(self):
# Function that saves the User to the Database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute('''
        INSERT INTO users (race, username, password, category) 
        VALUES (?, ?, ?,?)
        ''', (self.race, self.username, self.password, self.category))

        connection.commit()
        connection.close()

    @ui.page('/login')
    def login_page(self):
        with ui.card():
            ui.label("Login")
            username_input = ui.input(label="Username")
            password_input = ui.input(label="Password", password= True)

            def on_login():
                connection = sqlite3.connect("database.db")
                cursor = connection.cursor()

                cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?",
                               (username_input.value, password_input.value))
                user = cursor.fetchone()
                connection.close()

                if user:
                    ui.notify("Login successful")
                    ui.link("Go to Tasks", '/tasks')
                else:
                    ui.notify("Invalid credentials", color="red")

            ui.button("Login", on_click=on_login)
            ui.link("Register Here", '/register')
            #ui.link("Go to Tasks", '/tasks')

    @ui.page('/register')
    def get_information(self):
        # Function that creates a GUI and allows the user to input data
        with ui.card():
            ui.label("User Registration")
            ui.label("Select your Race")
            race_input = ui.select(
                label="Race",
                options=["Human", "Elve", "Orc", "Gnome", "Undead"],
                on_change=lambda: self.update_profile_img(race_input.value)
            )

            ui.label("Select your Class")
            category_input = ui.select(
                label="Class",
                options=["Knight", "Barbar", "Priest", "Rogue", "Mage"]
            )

            username_input = ui.input(label="Username")
            password_input = ui.input(label="Password", password=True)
            submit_input = ui.button("Submit", on_click=lambda: self.submit(race_input, username_input, password_input, category_input))
            ui.link("Go to Login", '/login')
            self.update_profile_img(race_input.value)

        return race_input, username_input, password_input, category_input

    def update_profile_img(self, race_input):
        if race_input == "Human":
            ui.image("media/Mensch.png")
        elif race_input == "Elve":
            ui.image("media/Elve.png")
        elif race_input == "Orc":
            ui.image("media/org.png")
        elif race_input == "Gnome":
            ui.image("media/gnom.png")
        elif race_input == "Undead":
            ui.image("media/untot.png")


    def submit(self, race_input, username_input, password_input, category_input):
# This Function is about the Button so that the user can be saved
        user = User(
            race=race_input.value,
            username=username_input.value,
            password=password_input.value,
            category=category_input.value
        )

        try:
            user.validate_input_types()
            user.save_to_db()
            ui.notify("User was saved Succesfully")

        except:
            ui.notify("User can not be saved in the Database")


user = User()
race_input, username_input, password_input, category_input= user.get_information()
