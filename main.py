#22 January 2022
#Author: Nasir Hossain Akash
#Python 3.8.2


import os
from pyrogram import Client

API_ID=os.getenv["API_ID"]
API_HASH=os.getenv["API_HASH"]
BOT_TOKEN=os.getenv["BOT_TOKEN"]
Username= os.getenv["USERNAME"]

app = Client("Telegram DM Forward Bot",api_id=int(API_ID),api_hash= API_HASH,bot_token=BOT_TOKEN)

@app.on_message()
async def my_handler(client, message):
    await message.forward(Username)

app.run()
