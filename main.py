import fastapi
from fastapi.middleware.cors import CORSMiddleware

import random

import hashlib
# import html

import sql


app = fastapi.FastAPI()

origins = [
    "http://127.0.0.1:5500",  # если запускаешь HTML через Live Server / локальный порт
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000/",
    "https://jsys12.github.io/SCAM.NET-site/",
    "https://jsys12.github.io/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,          # откуда разрешаем запросы
    allow_credentials=True,
    allow_methods=["POST", "GET", "OPTIONS"],            # какие методы (GET, POST, …)
    allow_headers=["Content-Type", "Authorization"],            # какие заголовки
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/insert_user/')
async def insert_user(username: str, gmail: str , password: str):

    sql.insert_user(username, gmail, password)
    return {"message": "User inserted successfully"}

@app.get('/select_user/')
async def select_user(username: str):
    result = sql.select_user_by_username(username)
    return {"username": username, "result": result}

@app.get('/select_user_password/')
async def select_user(username: str, password: str):
    result = sql.select_user_by_username_and_pass(username, password)
    return {"username": username, "result": result}



#@app.get('/select_all_users/')
#async def select_all_users():
#    return  sql.select_all_users()
