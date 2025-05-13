import mysql.connector
import csv
import uuid

def connect_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword",
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

def connect_to_prodev():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="yourpassword",
            database="ALX_prodev"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id VARCHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        )
    """)
    connection.commit()
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, filename):
    cursor = connection.cursor()
    with open(filename, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            user_id = str(uuid.uuid4())
            cursor.execute("""
                INSERT IGNORE INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (user_id, row["name"], row["email"], row["age"]))
    connection.commit()
    cursor.close()
