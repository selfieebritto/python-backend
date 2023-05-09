import sqlite3

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (email, password) VALUES (?, ?)',
                       (self.email, self.password))
        conn.commit()
        conn.close()
