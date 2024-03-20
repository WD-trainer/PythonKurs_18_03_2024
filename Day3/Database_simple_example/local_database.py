import sqlite3


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                age INTEGER
                            )''')
        self.conn.commit()

    def insert_user(self, user):
        self.cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (user.name, user.age))
        self.conn.commit()

    def fetch_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return [User(row[1], row[2]) for row in self.cursor.fetchall()]

    def close_connection(self):
        if self.conn:
            self.conn.close()

def main():
    db = Database('example.db')

    db.create_table()

    # db.insert_user(User('Alice', 30))
    # db.insert_user(User('Bob', 25))

    print("Users:")
    for user in db.fetch_all_users():
        print(f"Name: {user.name}, Age: {user.age}")

    db.close_connection()

if __name__ == "__main__":
    main()