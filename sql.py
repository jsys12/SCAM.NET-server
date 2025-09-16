import sqlite3 as sql
import json

connection = sql.connect("users.db")
cursor = connection.cursor()

def insert_user(username, gmail, password, ):
    cursor.execute("INSERT INTO users (username, gmail, password) VALUES (?, ?, ?)", (username, gmail, password))
    connection.commit()

def select_all_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return users

def select_user_by_username(username):
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    return user