import psycopg2
from pyrogram import Client, filters
from pyrogram.enums import ChatAction
from pyrogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton, CallbackQuery, ChatMember
import os

api_id = os.environ.get('api_id', 29864004)
api_hash = os.environ.get('api_hash', 'a22a8ed72778d57bf39aba4cb10bd776')
bot_token = os.environ.get('bot_token', '7336131245:AAFI-4ufFhiJjO6GcU9ZfvIgyuxRQRHYZqk')


proxy = {
    "scheme": "socks4",  # "socks4", "socks5" and "http" are supported
    "hostname": "127.0.0.1",
    "port": 2080,
}

plugins = dict(root='django_bot/plugins')

api = Client(
    name='py_django',
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token,
    proxy=proxy,
    plugins=plugins,
)


def check_join(_, client: Client, message: Message):
    try:
        client.get_chat_member(chat_id='@amin_django_python', user_id=message.from_user.id)
        return True

    except:
        message.reply_text(text='به ربات انجام پروژه پایتون و جنگو خوش آمدید\nبرای کار کردن با ربات عضو چنل شوید',
                           reply_markup=InlineKeyboardMarkup(
                               [[
                                    InlineKeyboardButton(text='چنل انجام پروژه پایتون و جنگو',
                                                          url='https://t.me/amin_django_python')
                                ],
                                [
                                    InlineKeyboardButton(text='عضو شدم', callback_data='check'),
                                ]]
                           ))
        return False


check_join = filters.create(check_join)


@api.on_callback_query()
async def check_callback_query(client: Client, c: CallbackQuery):
    if c.data == 'check':
        try:
            await client.get_chat_member(chat_id='@amin_django_python', user_id=c.from_user.id)
            await c.message.reply_text('عضویت شما با موفقیت تایید شد')

        except:
            await c.message.delete()
            await c.message.reply(text='شما عضو کانال نشده اید\nبرای کار کردن با ربات عضو چنل شوید',
                                reply_markup=InlineKeyboardMarkup(
                                   [
                                       [
                                           InlineKeyboardButton(text='چنل انجام پروژه پایتون و جنگو',
                                                              url='https://t.me/amin_django_python')
                                       ],
                                       [
                                           InlineKeyboardButton(text='عضو شدم', callback_data='check'),
                                       ]
                                       ]
                                ))

    elif c.data == '':
        pass


@api.on_message(filters=filters.command('start') & check_join)
async def start(client: Client, message: Message):
    await message.reply_text('نوع پروژه خود را انتخاب کنید', reply_markup=ReplyKeyboardMarkup(
        [
            ['پروژه پایتون'],
            ['پروژه جنگو'],
            ['پروژه ربات تلگرام'],
        ], resize_keyboard=True
    ))


@api.on_message(filters=filters.text)
async def check_text(client: Client, message: Message):
    if message.text == 'پروژه پایتون':
        await message.reply_text('عنوان پروژه:')
        dict_py = {
            'title': message.text
        }
    elif message.text == 'پروژه جنگو':
        await message.delete()
        dict_py = {
            'title': message.text
        }
        await message.reply_text('عنوان پروژه خود را انتخاب کنید', reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='وب سایت فروشگاهی', callback_data='web_store')
                ],
                [
                    InlineKeyboardButton(text='وب سایت وبلاگ', callback_data='blog')
                ],
                [
                    InlineKeyboardButton(text='وب سایت پیام رسان', callback_data='messanger')
                ],
                [
                    InlineKeyboardButton(text='وب سایت  فیلم و سریال', callback_data='messanger')
                ]
            ]
        ))

    elif message.text == 'پروژه ربات تلگرام':
        dict_py = {
            'title': message.text
        }
        await message.reply_text('عنوان پروژه خود را انتخاب کنید', reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='ربات تبلیغ', callback_data='web_store')
                ],
                [
                    InlineKeyboardButton(text='ربات چت ناشناس', callback_data='blog')
                ],
                [
                    InlineKeyboardButton(text='ربات سلف', callback_data='messanger')
                ]
            ]
        ))

api.run()