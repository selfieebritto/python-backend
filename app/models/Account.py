import sqlite3

class User:
    def __init__(self, name, email, password, salt, status):
        self.email = email
        self.password = password
        self.name = name
        self.salt = salt
        self.status = status

    def save(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name,email, password,salt,status) VALUES (?, ?, ?, ?, ?)',
                       (self.name, self.email, self.password, self.salt, self.status))
        conn.commit()
        conn.close()
