import sqlite3

from db.models import User


def connect(db_name="db.sqlite3"):
    con = sqlite3.connect(db_name)
    return con


def create_users_table(con):
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            token TEXT UNIQUE
        )"""
    )
    con.commit()


def create_user(con, name, token):
    cur = con.cursor()
    cur.execute("""INSERT INTO users (name, token) VALUES (?, ?)""", (name, token))
    con.commit()


def get_user(con):
    cur = con.cursor()
    cur.execute("""SELECT * FROM users""")
    return User(*cur.fetchone())


def get_user_by_token(con, token):
    cur = con.cursor()
    cur.execute("""SELECT * FROM users WHERE token = ?""", (token,))
    return User(*cur.fetchone())


def disconnect(con):
    return con.close()


def migrate():
    con = connect()
    create_users_table(con)
    disconnect(con)