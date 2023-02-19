import os
import aiohttp
import time
from pymongo import MongoClient
from datetime import datetime
from server.response_helper import *
from dotenv import load_dotenv
from time import sleep
from server.controllers.notification.bot_moisture import send_message
from server.controllers.config_value import *

env = load_dotenv()

# mongodb connection
# attempt fails
max_retries = 5
num_fails = 0
try:
    client = MongoClient(os.getenv("MONGO_URI"), serverSelectionTimeoutMS=10000, connectTimeoutMS=10000, maxPoolSize=20, waitQueueTimeoutMS=10000)
    db = client[os.getenv("DATABASE")]
    collection = db.moisture
except Exception as e:
    num_fails += 1
    print(f"{e} attempt fail {num_fails}")
    if num_fails > max_retries:
        raise e
    sleep(0.5)

# BASE URL
base_url = os.getenv("BASE_URL")


async def get_all_moisture_cabai():
    datas = []
    result = collection.find({"tanaman": "cabai"}).sort("created_at", -1)
    for x in result:
        datas.append({
            "tanaman": x.get("tanaman"),
            "value": x.get("value"),
            "created_at": x.get("created_at"),
            "fetch_time": x.get("fetch_time")
        })
    return datas


async def get_moisture_cabai():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{base_url}/moisture") as response:
            resp = await response.json()
            value = resp.get("value")
            collection.insert_one({
                "tanaman": "cabai",
                "value": value,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "fetch_time": f"{round(time.time() - start_time, 2)}"
            })
            datas = {
                "tanaman": "cabai",
                "value": value,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "fetch_time": f"{round(time.time() - start_time, 2)}"
            }
            if value < limit_moisture_cabai:
                await send_message(datas)
            return datas
