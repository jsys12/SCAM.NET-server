import sqlite3 as sql
import json
import hash

connection = sql.connect("users.db")
cursor = connection.cursor()

def insert_user(username, gmail, password):
    hash_param = hash.hash_password(password)
    hash_pass= hash_param["h_pass"]
    salt = hash_param["salt"]
    cursor.execute("INSERT INTO users (username, gmail, hash_pass, salt) VALUES (?, ?, ?, ?)", (username, gmail, hash_pass, salt))
    connection.commit()

def select_all_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    return users

def select_user_by_username(username):
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    return user