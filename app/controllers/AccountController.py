
import sqlite3

from app.models.Account import User

def register_user(email, password):
    user = User(email, password)
    user.save()

def validate_user(username, password):
    conn = sqlite3.connect('database.db')  # Replace with your SQLite database file path
    cursor = conn.cursor()

    # Execute a query to fetch the user with the provided username and password
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()

    return user

def get_all_users():
    conn = sqlite3.connect('database.db')  # Replace with your SQLite database file path
    cursor = conn.cursor()

    # Execute a query to fetch the user with the provided username and password
    cursor.execute("SELECT * FROM users")
    user = cursor.fetchall()

    conn.close()

    return user    