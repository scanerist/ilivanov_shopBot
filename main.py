from aiogram import types, Bot, Dispatcher, fsm
from aiogram.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import requests

import xml.etree.ElementTree as ET
import logging

from config import Config, load_config

command_dict = {"clothes": False,
                "shoes": False}


class FSMfill(StatesGroup):
    fill_shoes_price = State()
    fill_accesories_price = State()


kb = [[KeyboardButton(text='Рассчитать обувь💵')],
      [KeyboardButton(text='Рассчитать одежду💴')],
      [KeyboardButton(text='Помощь❓')],
      [KeyboardButton(text='Отзывы✉️')], ]
config: Config = load_config()
BOT_TOKEN: str = config.tg_bot.token
print(BOT_TOKEN)
logging.basicConfig(level=logging.INFO)

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


def cny_to_rub_converter(value: int) -> float:
    cny_rate = float(
        ET.fromstring(requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text)
        .find("./Valute[CharCode='CNY']/Value")
        .text.replace(",", ".")) + 1
    return cny_rate * value


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f'Привет, @{message.from_user.full_name} \n'
                         f'<b>ilivanovshopbot</b> поможет тебе рассчитать сумму твоего заказа', reply_markup=keyboard,
                         parse_mode='HTML')


@dp.message(Text(text="Рассчитать обувь💵"))
async def send_shoe_command(message: Message):
    command_dict["shoes"] = True
    await message.answer(f"Ведите сумму для перевода , актуальный курс: <b>{round(cny_to_rub_converter(1), 2)}</b>",
                         parse_mode='HTML')


@dp.message(Text(text="Рассчитать одежду💴"))
async def send_accesories_command(message: Message):
    command_dict["clothes"] = True
    await message.answer(f"Ведите сумму для перевода, актуальный курс: <b>{round(cny_to_rub_converter(1), 2)}</b>",
                         parse_mode='HTML')


@dp.message(Text(text='Помощь❓'))
async def process_help_command(message: Message):
    await message.answer(f'<b>ilivanovshopbot</b> поможет тебе рассчитать сумму твоего заказа',
                         reply_markup=ReplyKeyboardMarkup(keyboard=kb), parse_mode='HTML')


@dp.message(Text(text='Отзывы✉️'))
async def process_help_command(message: Message):
    await message.answer(f'отзывы: https://vk.com/wall303473975_327',
                         reply_markup=ReplyKeyboardMarkup(keyboard=kb, ))


@dp.message()
async def answer_convert(message: types.Message):
    user_mes = int(message.text)
    conversion_output: float = round(cny_to_rub_converter(user_mes), 2)
    if command_dict["clothes"]:
        await message.answer(
            f"Сумма составляет: <b>{round(conversion_output + conversion_output * 0.15 + 700, 4)} RUB</b>\n\n"
            f"❗️<b>ЭТА СУММА С УЧЕТОМ ДОСТАВКИ И КОМИССИИ</b>❗️",
            reply_markup=ReplyKeyboardMarkup(keyboard=kb), parse_mode='HTML')
        command_dict["clothes"] = False
    if command_dict["shoes"]:
        await message.answer(
            f"Сумма составляет: <b>{round(conversion_output + conversion_output * 0.15 + 1200, 4)} RUB</b>\n\n"
            f"❗️<b>ЭТА СУММА С УЧЕТОМ ДОСТАВКИ И КОМИССИИ</b>❗️", parse_mode='HTML')
        command_dict["shoes"] = False


if __name__ == '__main__':
    dp.run_polling(bot)
