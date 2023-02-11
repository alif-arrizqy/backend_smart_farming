import os
import requests
from dotenv import load_dotenv

env = load_dotenv()
TOKEN_BOT = os.getenv("TOKEN_BOT")
USER_CHAT_ID = os.getenv("USER_CHAT_ID")


async def send_message(data):
    url = f"https://api.telegram.org/bot{TOKEN_BOT}/sendMessage"
    
    tanaman = data.get("tanaman")
    value = data.get("value")
    msg = f' Hi Farmer, suhu udara saat ini adalah {value}℃ \n' \
    f'Sebaiknya segera melakukan penyiraman pada tanaman {tanaman}.'

    payload = {
        "text": msg,
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": None,
        "chat_id": USER_CHAT_ID
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)