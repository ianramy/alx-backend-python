import sqlite3


class ExecuteQuery:
    def __init__(self, query, params=None, db_name="users.db"):
        self.query = query
        self.params = params or []
        self.db_name = db_name
        self.connection = None
        self.result = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        cursor = self.connection.cursor()
        cursor.execute(self.query, self.params)
        self.result = cursor.fetchall()
        return self.result

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()


# Usage example
if __name__ == "__main__":
    query = "SELECT * FROM users WHERE age > ?"
    params = [25]
    with ExecuteQuery(query, params) as results:
        for row in results:
            print(row)
