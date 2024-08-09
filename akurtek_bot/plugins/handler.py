from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup


@Client.on_message(filters=filters.command('start'))
async def start(client: Client, message: Message):
    await message.reply_text('sm')


@Client.on_message(filters=filters.command('first'))
async def start(client: Client, message: Message):
    await message.reply_text('sa', reply_markup=ReplyKeyboardMarkup([['1', '2']]))
