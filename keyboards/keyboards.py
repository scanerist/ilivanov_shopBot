from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


builder = ReplyKeyboardBuilder()

kb = builder.row(KeyboardButton(text='Рассчитать обувь💵', ),
                 KeyboardButton(text='Рассчитать одежду, аксессуары💴'))
kb2 = builder.row(KeyboardButton(text='Отзывы✉️'),
                  KeyboardButton(text='Часто задаваемые вопросы❗'))