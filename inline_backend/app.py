import config
import time
import httpx
from db import redis_db
from fastapi import FastAPI
from models import SearchResponse

app = FastAPI()


@app.get("/search/{item}")
async def search(item: str):
    cached = redis_db.get(item)

    if cached is None:
        async with httpx.AsyncClient() as client:
            response = await client.get(config.GITHUB_API_URL + item)
        raw_data = response.content
        redis_db.set(item, raw_data)
    else:
        raw_data = cached.decode("utf-8")

    return SearchResponse.parse_raw(raw_data)
