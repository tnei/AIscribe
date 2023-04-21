import config
from fastapi import FastAPI

app = FastAPI()

@app.get("/get-api-key")
async def get_api_key():
    return {"api_key": config.API_KEY}
