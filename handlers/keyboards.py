from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup,
                           CallbackQuery)
                           
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



main = InlineKeyboardMarkup(inline_keyboard=[

    [
        InlineKeyboardButton(text="📝 Добавить расход", callback_data="add_expense"),
        InlineKeyboardButton(text="📊 Статистика", callback_data="view_stats")
    ], 

    [
        InlineKeyboardButton(text="⚙️Настройки", callback_data="settings")
    ]
])

def back_to_main():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад в меню", callback_data="go_to_main")]
        ])

def back_to_settings():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Назад", callback_data="settings")]
        ])

menu_settings = {"👤 Профиль": "open_profile", 
                      "❓ Помощь": "open_help", 
                      "⬅️ Назад": "go_to_main"
                      }


async def settings_buttons():
    keyboard = InlineKeyboardBuilder()
    for text, callback in menu_settings.items():
        keyboard.add(InlineKeyboardButton(text=text, callback_data=callback))
    return keyboard.adjust(2).as_markup()