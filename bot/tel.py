from telethon import TelegramClient, events, Button
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.users import GetFullUserRequest
import socks
from asyncio import sleep

client = TelegramClient('bot_session', api_hash='a22a8ed72778d57bf39aba4cb10bd776', api_id=29864004, proxy=(socks.SOCKS4, '127.0.0.1', 2080, True))


@client.on(events.MessageDeleted())
async def start(event):
    chat = 'kkk'
    markup = client.build_reply_markup(
        [
            Button.inline('فارسی'),
            Button.inline('english')
        ]
    )
    await client.send_message(entity=event.chat_id, message=f'{chat}سلا', buttons=markup)


@client.on(events.NewMessage(pattern=r'/first'))
async def first(event):
    markup = client.build_reply_markup(
        [
            Button.inline('english', data='test'),
        ]
    )
    await client.send_message(entity=event.chat_id, message='ربان هود را انتخاب کنید', buttons=markup)


@client.on(events.CallbackQuery(data='test'))
async def callback_query(event):
    await client.send_message(event.chat_id, message='onnj')

client.start(bot_token='6801305177:AAHjAdN2B6M5DRp8mLc7Z4dOSPzcNFAGwv4')

client.run_until_disconnected()
