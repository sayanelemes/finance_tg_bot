from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup,
                           CallbackQuery)
                           
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from database.requests import get_categories


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



async def categories_keyboard():
    keyboard = InlineKeyboardBuilder()
    categories = await get_categories()
    
    for category in categories:
        keyboard.add(InlineKeyboardButton(
            text=category.name, 
            callback_data=f"category_{category.id}"))

    keyboard.adjust(2)


    keyboard.attach(InlineKeyboardBuilder.from_markup(back_to_main()))
    return keyboard.as_markup()