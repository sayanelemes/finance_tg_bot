from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_keyboard():
    rpls = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 СТАТУС СЕРВЕРА")]
        ],   
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )
    return rpls