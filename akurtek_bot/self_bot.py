from pyrogram import Client
from pyrogram.types import Message
from datetime import datetime
import os

proxy = {
     "scheme": "socks4",  # "socks4", "socks5" and "http" are supported
     "hostname": "127.0.0.1",
     "port": 2080,
 }

api = Client(
    'self_bot',
    api_id=29864004,
    api_hash='a22a8ed72778d57bf39aba4cb10bd776',
    proxy=proxy
)


async def main():
    async with api:
        await api.update_profile(bio=str(datetime.today().time()))


api.run(main())

