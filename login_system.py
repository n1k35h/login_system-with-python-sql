import sqlite3

CREATE_LOGIN_TABLE = """ CREATE TABLE IF NOT EXISTS login (
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
);"""

INSERT_LOGIN = "INSERT INTO login (username, password) VALUES (?, ?);"

GET_ALL_LOGIN = "SELECT * FROM login WHERE username=? and password=?;"

def connect():
    # connection = sqlite3.connect("logindb.db")
    # print("Database is connected")
    
    return sqlite3.connect("logindb.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_LOGIN_TABLE)

def add_login(connection, username, password):
    with connection:
        connection.execute(INSERT_LOGIN, (username, password))

def get_all_login(connection, username, password):
    with connection:
        return connection.execute(GET_ALL_LOGIN, (username, password,)).fetchone()