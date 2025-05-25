import sqlite3


class DatabaseConnection:
    def __init__(self, db_name="users.db"):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        # Open database connection
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        # Close database connection
        if self.connection:
            self.connection.close()


# Usage example
if __name__ == "__main__":
    with DatabaseConnection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)
