from aiogram import Bot, Dispatcher, types
import asyncio
from random import randint
import importlib
import os

Token = '7901460835:AAEZCbVuEebbwTLTXEar7E7ohuVzKVxuWfk'  # токен бота
channel = '@zayavki_u'  # ссылка на канал

bot = Bot(token=Token)  # создаем бот
dp = Dispatcher()  # управление сообщениями

user_data = {}
project_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(project_dir, 'images')  # путь к картинкам


@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    if message.text == '/start':
        await welcome(message)


async def welcome(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {}
    button = [
        [
            types.KeyboardButton(text='Русский 🇷🇺'),
            types.KeyboardButton(text='English 🇬🇧'),
            types.KeyboardButton(text='Uzbekcha 🇺🇿')
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)

    await message.answer('Добро пожаловать в наш бот!\nВыберите язык', reply_markup=keyboard)
