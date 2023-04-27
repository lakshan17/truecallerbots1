import os
import json
import requests
from Config import *
from pyrogram import Client, filters

url = "https://api4.truecaller.com/v1/search"

headers = {
    "Accept": "application/json",
    "User-Agent": "Truecaller/11.52.5",
    "Authorization": f"Bearer {API_KEY}"
}

app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

@app.on_message(filters.command("search"))
def search(client, message):
    try:
        phone_number = message.text.split(" ")[1]
        params = {
            "type": "4",
            "countryCode": "PH",
            "q": phone_number
        }
        response = requests.get(url, headers=headers, params=params) 
        data = response.json()
        result = data["data"][0]
        text = f"Name: {result['name']}\nLocation: {result['location']}\nCarrier: {result['carrier']}"
        message.reply(text)
    except Exception as e:
        app.send_message(LOG_CHANNEL, f"An error occurred: {str(e)}")

app.run()