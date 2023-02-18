from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import kb, kb2
from lexicon.lexicon import LEXICON_RU
from services.services import cny_to_rub_converter

router: Router = Router()

command_dict = {"clothes": False,
                "shoes": False}


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=kb.as_markup(resize_keyboard=True), parse_mode='HTML')


@router.message(Text(text=LEXICON_RU['shoes']))
async def shoes_currency(message: Message):
    command_dict["shoes"] = True
    await message.answer(text=LEXICON_RU['Рассчитать обувь💵'], parse_mode='HTML')


@router.message(Text(text=LEXICON_RU['clothes']))
async def clothes_currency(message: Message):
    command_dict["clothes"] = True
    await  message.answer(text=LEXICON_RU['Рассчитать одежду, аксессуары💴'], parse_mode='HTML')


@router.message(Text(text=LEXICON_RU['feedback']))
async def process_feedback_command(message: Message):
    await message.answer(text=LEXICON_RU['Отзывы✉️'],
                         reply_markup=kb.as_markup(resize_keyboard=True))


@router.message(Text(text=LEXICON_RU['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['Часто задаваемые вопросы❗'], reply_markup=kb.as_markup(resize_keyboard=True))


@router.message()
async def answer_convert(message: Message):
    if command_dict["shoes"] and command_dict["clothes"]:
        command_dict["clothes"] = False
        command_dict["shoes"] = False
        await message.answer(text=LEXICON_RU['error'], reply_markup=kb.as_markup(resize_keyboard=True))

    user_mes = int(message.text)
    conversion_output: float = round(cny_to_rub_converter(user_mes), 2)
    if command_dict["clothes"]:
        command_dict["clothes"] = False
        await message.answer(
            f"Сумма составляет: <b>{round(conversion_output + conversion_output * 0.15 + 700, 4)} RUB</b>\n\n"
            f"❗️<b>ЭТА СУММА С УЧЕТОМ ДОСТАВКИ ДО СПБ И КОМИССИИ</b>❗\n"
            f"️❗️Доствка в регионы происходит по СДЭК❗\n\n"
            f"для оформления пиши менеджеру\n🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽\n\n\n"
            f"https://t.me/ivnvilyapzn", parse_mode='HTML', )

    if command_dict["shoes"]:
        command_dict["shoes"] = False
        await message.answer(
            f"Сумма составляет: <b>{round(conversion_output + conversion_output * 0.15 + 1200, 4)} RUB</b>\n\n"
            f"❗️<b>ЭТА СУММА С УЧЕТОМ ДОСТАВКИ ДО СПБ И КОМИССИИ</b>❗\n"
            f"️❗️Доствка в регионы происходит по СДЭК❗\n\n"
            f"ДЛЯ ОФОРМЛЕНИЯ ПИШИ МЕНЕДЖЕРУ\n🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽🔽\n\n\n"
            f"https://t.me/ivnvilyapzn",
            parse_mode='HTML'
        )
