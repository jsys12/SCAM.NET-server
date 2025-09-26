import hashlib
import os
# import random



# password = "password123"
#
# byte_password = password.encode('utf-8')
#
# hash_password = hashlib.sha256(byte_password).hexdigest()
#
# print(hash_password)

def hash_password(password: str, salt = os.urandom(64)):
    """"
    Принимает пароль

    Возвращяет хеш пароля с солью
    """

    password = password.encode('utf-8')
    hashed_password = hashlib.scrypt(password, salt=salt, n=16384, r=8, p=1)
    return {"h_pass": hashed_password.hex(), "salt": salt}

def chek_password(password: str, salt: bytes, hash_p: str):
    """"
    Принимает пароль + соль и хешированный пароль

    Возвращяет, правильный пароль или нет
    """
    if hash_password(password, salt)["h_pass"] == hash_p:
        return True
    return False

# result1 = hash_password(input("Password1: "))
# print(result1)
# result2 = hash_password(input("Password2: "), result1["salt"])
# print(result2)

