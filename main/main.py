from user import User  #Import User Class
import sqlite3
import database  #Import Database

def main():
    database.setup_database()

    user = User().create_user()
    print(user)

    user.save_to_db()

if __name__ == "__main__":
    main()