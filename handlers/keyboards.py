from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
                           
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📝 Добавить расход', callback_data='add_expence'),
    InlineKeyboardButton(text='📊 Статистика', callback_data='view_stats'),
    InlineKeyboardButton(text='Настройки', callback_data='settings')]
    ])



test = ['Профиль', 'Помощь', 'test']


async def inline_test():
    keyboard = InlineKeyboardBuilder()
    for example in test:
        keyboard.add(InlineKeyboardButton(text=example, url='https://github.com/sayanelemes'))
    return keyboard.adjust(3).as_markup()