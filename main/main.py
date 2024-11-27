from user import User  #Import User Class
import database  #Import Database
import sqlite3

def main():
    database.setup_database()

    user = User().create_user()
    print(user)

    user.save_to_db()

if __name__ == "__main__":
    main()