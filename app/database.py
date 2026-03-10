import sqlite3

DB_PATH = "users.db"

def get_connection():

    return sqlite3.connect(DB_PATH)


def get_user(username, password):

    conn = get_connection()

    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    result = cursor.execute(query).fetchone()

    conn.close()

    return result