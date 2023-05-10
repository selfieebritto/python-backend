
import sqlite3

from bcrypt import checkpw

from app.models.Account import User

def register_user(name, email, password, salt, status):
    user = User(name, email, password, salt, status)
    user.save()

def validate_user(username, password):
    conn = sqlite3.connect('database.db')  # Replace with your SQLite database file path
    cursor = conn.cursor()

    # Execute a query to fetch the user with the provided username and password
    cursor.execute("SELECT password,salt FROM users WHERE email=?", (username,))
    user = cursor.fetchone()
    print(user)
    if user:
        hashed_password = user[0]
        salt = user[1]

        # Check if the entered password matches the stored password
        if checkpw(password.encode('utf-8'), hashed_password):
            conn.close()
            return True
    conn.close()

    return False

def get_all_users():
    conn = sqlite3.connect('database.db')  # Replace with your SQLite database file path
    cursor = conn.cursor()

    # Execute a query to fetch the user with the provided username and password
    cursor.execute("SELECT * FROM users")
    user = cursor.fetchall()

    conn.close()

    return user    

def getUserByEmail(email):
    conn = sqlite3.connect('database.db')  # Replace with your SQLite database file path
    cursor = conn.cursor()

    # Execute a query to fetch the user with the provided username and password
    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()
    # print(user)
    if user:
        return user
    conn.close()

    return False