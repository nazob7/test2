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

print('hello world')
print('hello world')
print('hello world')
print('hello world')
print('hello world')

@dp.message()
async def handle_message(message: types.Message):
    user_id = message.from_user.id
    if message.text == '/start':
        await welcome(message)
    elif 'lang' not in user_data[user_id]:
        await check_language(message)
    elif 'phone' not in user_data[user_id]:
        await check_phone(message)
    elif 'status' not in user_data[user_id]:
        await check_code(message)
    elif 'categories' in user_data[user_id]['state']:
        await show_menu(message)
    elif 'delivery' in user_data[user_id]['state']:
        await pickup(message)
    elif 'pickup' in user_data[user_id]['state']:
        await show_categories(message)
    elif 'items' in user_data[user_id]['state']:
        await show_items(message)
    elif 'item' in user_data[user_id]['state']:
        await preview_item(message)
    elif 'preview' in user_data[user_id]['state']:
        await basket_m(message)
    elif 'settings' in user_data[user_id]['state']:
        await edit_phone(message)
    elif 'edit_phone' in user_data[user_id]['state']:
        await phone_ver(message)
    elif 'edit_phone_ver' in user_data[user_id]['state']:
        await check_v_phone(message)
    elif 'fdb' in user_data[user_id]['state']:
        await save_fdb(message)
    elif 'cart' in user_data[user_id]['state']:
        await cart_order(message)


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


def select_language(lang):
    if lang == 'Русский 🇷🇺':
        return 'ru'
    elif lang == 'English 🇬🇧':
        return 'en'
    elif lang == 'Uzbekcha 🇺🇿':
        return 'uz'


async def check_language(message: types.Message):
    user_id = message.from_user.id
    lang = message.text
    lang = select_language(lang)
    user_data[user_id]['lang'] = lang
    lang = importlib.import_module(f'lang.{lang}')
    btn = [[
        types.KeyboardButton(text=lang.phone_button, request_contact=True)
    ]]

    keyboard = types.ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)

    await message.answer(f'{lang.phone_text}', reply_markup=keyboard)

async def check_phone(message: types.Message):
    user_id = message.from_user.id
    lang = user_data[user_id]['lang']
    lang = importlib.import_module(f'lang.{lang}')
    if message.contact is not None:
        phone = message.contact.phone_number
    else:
        phone = message.text
    user_data[user_id]['phone'] = phone
    verification_code = randint(100000, 999999)
    user_data[user_id]['ver_code'] = verification_code
    await message.answer(f'{lang.ver_text} {verification_code}')
