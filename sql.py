import sqlite3 as sql
import json
import hash
import re
import time

connection = sql.connect("users.db")
cursor = connection.cursor()


def validation_check(username, password, gmail):
    errors = []

    # # Валидация username: мин. 5 символов, только alnum, без пробелов, уникальность в БД
    # if len(username) < 5:
    #     errors.append("Username должен быть не менее 5 символов")
    # if not username.replace(" ", "").isalnum():
    #     errors.append("Username может содержать только буквы и цифры, без пробелов")
    # existing_user = select_user_by_username(username)
    # if existing_user is not None:
    #     errors.append("Username уже существует")
    #
    # # Валидация password: 6-20 символов, upper, lower, digit, special (@$#%)
    # if len(password) < 6 or len(password) > 20:
    #     errors.append("Пароль должен быть от 6 до 20 символов")
    # if not re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d@$#%]{6,20}$", password):
    #     errors.append("Пароль должен содержать заглавную букву, строчную, цифру и специальный символ (@, $, #, %)")
    #
    # # Валидация gmail: формат email, популярные домены, уникальность
    # email_pattern = r"^[a-zA-Z0-9._%+-]+@(gmail|yahoo|outlook|hotmail|aol|mail|yandex)\.com$"
    # if not re.match(email_pattern, gmail):
    #     errors.append(
    #         "Email должен быть в формате example@домен.com, где домен: gmail, yahoo, outlook, hotmail или aol")
    # # Проверка уникальности gmail
    # cursor.execute("SELECT * FROM users WHERE gmail = ?", (gmail,))
    # if cursor.fetchone():
    #     errors.append("Email уже зарегистрирован")

    if errors:
        return False
    return True


def insert_user(username, gmail, password, token, token_life):
    try:
        if(validation_check(username, password, gmail)):
            hash_param = hash.hash_password(password)
            hash_pass= hash_param["h_pass"]
            salt = hash_param["salt"]
        else:
            return {"Error": "Invalid username | password or something gay happened"}

        cursor.execute("INSERT INTO users (username, gmail, hash_pass, salt, auth_token, auth_token_lifetime) VALUES (?, ?, ?, ?, ?, ?)", (username, gmail, hash_pass, salt, token, token_life))
        connection.commit()
    except:
        return {"Error": "Invalid username | password or something gay happened"}

# def select_a ll_users():
#     cursor.execute("SELECT * FROM users")
#     users = cursor.fetchall()
#     return users

def select_user_by_username(username):
    try:
        cursor.execute("SELECT username, gmail, id FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        return user
    except:
        return {"Error": "User not found or something gay happened"}

def select_user_by_username_and_pass(username, password):
    try:
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = list(cursor.fetchone())
        result = hash.chek_password(password, user[4], user[3])
        user[4] = str(user[4])
        if result:
            return {"username": user[1], "gmail": user[2], "id": user[0]}
        else:
            return {"Error": "Password doesn't match"}
    except:
        return {"Error": "Password | username doesn't match or something gay happened"}



