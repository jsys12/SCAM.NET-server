import fastapi

import html


app = fastapi.FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World" * 100}
