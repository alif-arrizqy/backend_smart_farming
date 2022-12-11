import os
import aiohttp
import asyncio
import time
from pymongo import MongoClient
from datetime import datetime
from server.response_helper import *
from dotenv import load_dotenv

env = load_dotenv()

# mongodb
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DATABASE")]
collection = db.humidity

# BASE URL
base_url = os.getenv("BASE_URL")


async def get_all_humidity():
    datas = []
    result = collection.find()
    for x in result:
        datas.append({
            "humidity": x.get("value"),
            "created_at": x.get("created_at"),
        })
    return datas


async def get_humidity():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{base_url}/humidity") as response:
            resp = await response.json()
            collection.insert_one({
                "value": resp["value"],
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "fetch_time": f"{round(time.time() - start_time, 2)}"
            })
            datas = {
                "value": resp["value"],
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "fetch_time": f"{round(time.time() - start_time, 2)}"
            }
            return datas


async def store_humidity(value):
    collection.insert_one({
        "value": value.get("value"),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    datas = {
        "value": value.get("value"),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return datas
    