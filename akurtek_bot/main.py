from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import os

plugins = dict(root="plugins")

api_id = os.environ.get('api_id', 29864004)
api_hash = os.environ.get('api_hash', 'a22a8ed72778d57bf39aba4cb10bd776')
bot_token = os.environ.get('bot_token', '7215128406:AAETDP6YmTb41OEV01-InxoDZKjScwClKl8')

proxy = {
     "scheme": "socks4",  # "socks4", "socks5" and "http" are supported
     "hostname": "127.0.0.1",
     "port": 2080,
 }

app = Client(
    'akurtek',
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    proxy=proxy,
)


@app.on_message(filters=filters.command('first'))
async def start(client: Client, message: Message):
    await message.reply_text('sa', reply_markup=ReplyKeyboardMarkup([['1', '2'], ['3', '4']], resize_keyboard=True))


@app.on_message(filters=filters.command('remove'))
async def start(client: Client, message: Message):
    await message.reply_text('delete buttons', reply_markup=ReplyKeyboardRemove())


@app.on_message(filters=filters.command('second'))
async def start(client: Client, message: Message):
    print(message)
    print('*' * 20)
    print(client)
    await message.reply_text('sa', reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text='1', callback_data='data1'),
                InlineKeyboardButton(text='2', callback_data='data2')
            ],
            [
                InlineKeyboardButton(text='3', url='https://t.me/amin_django_python'),
            ]
        ]
    ))


@app.on_callback_query()
async def callback_query(client: Client, c:CallbackQuery):
    if c.data == 'data2':
        await c.message.reply_text('you clicked button 2')


@app.on_message(filters.command('photo'))
async def on_message(client: Client, message: Message):
    await message.reply_photo('/home/amin/Pictures/Screenshots/Screenshot from 2024-07-30 01-45-42.png', caption='photo')
    await message.reply_photo('https://assets.goal.com/images/v3/bltecd725ea01dc56af/ONLY_GERMANY_Zinedine_Zidane_2023.jpg?auto=webp&format=pjpg&width=3840&quality=60',
                              caption='photo')
    await message.reply_chat_action(action=ChatAction.UPLOAD_PHOTO)


@app.on_message(filters.command('video'))
async def on_message(client: Client, message: Message):
    try:
        await message.reply_video('https://youtu.be/_pgqSlXIvTw?si=UXvuAHpLb0TrhE-y',
                              thumb='https://assets.goal.com/images/v3/bltecd725ea01dc56af/ONLY_GERMANY_Zinedine_Zidane_2023.jpg?auto=webp&format=pjpg&width=3840&quality=60',
                              caption='zidane video')
    except:
        await message.reply_text('cant upload')

    await message.reply_video('https://t.me/azar_ragse/67881')
    await message.reply_chat_action(action=ChatAction.UPLOAD_PHOTO)


@app.on_message()
async def on_message(client: Client, message: Message):
    await app.send_message(chat_id='@amin_django', text='hello django developer')


