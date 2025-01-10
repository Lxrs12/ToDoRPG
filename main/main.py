import database  # Import Database
from user import User  # Import User Class
import sqlite3

def main():
    database.setup_database()

if __name__ == "__main__":
    main()
