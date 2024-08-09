from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import os
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

api_id = os.environ.get('api_id', 29864004)
api_hash = os.environ.get('api_hash', 'a22a8ed72778d57bf39aba4cb10bd776')
bot_token = os.environ.get('bot_token', '7215128406:AAETDP6YmTb41OEV01-InxoDZKjScwClKl8')

proxy = {
     "scheme": "socks4",  # "socks4", "socks5" and "http" are supported
     "hostname": "127.0.0.1",
     "port": 2080,
 }

api = Client(
    'akurtek',
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    proxy=proxy,
)


@api.on_message(filters=filters.text)
async def on_message(client: Client, message: Message):
    if message.text == 'ارز':
        price = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies='usd')
        await message.reply_text(f'bitcoin:{price["bitcoin"]["usd"]}')


api.run()
