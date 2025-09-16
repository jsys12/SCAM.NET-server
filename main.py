import fastapi

# import html

import sql


app = fastapi.FastAPI()


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

#@app.get('/select_all_users/')
#async def select_all_users():
#    return  sql.select_all_users()
