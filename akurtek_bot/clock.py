import datetime
import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client

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

iran = pytz.timezone('Asia/Tehran')


async def main():
    date = datetime.datetime.now(tz=iran).strftime('%H:%M:%S')
    await api.update_profile(bio=str(date))


scheduler = AsyncIOScheduler()

scheduler.add_job(main, 'interval', seconds=10)

scheduler.start()

api.run()