import handlers.keyboards as kb


from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Добро пожаловать в финбот!",
        reply_markup=kb.main
    )




@router.callback_query(F.data == "settings")
async def show_settings(callback: CallbackQuery):
    await callback.answer("⚙️Настройки")
    await callback.message.edit_text("⚙️Настройки:", reply_markup=await kb.settings_buttons())

@router.callback_query(F.data == "open_profile")
async def show_profile(callback: CallbackQuery):
    await callback.answer()
    
    user_name = callback.from_user.first_name
    user_id = callback.from_user.id

    profile_text = (
        f"👤Ваш Профиль:\n"
        f"Имя: {user_name}\n"
        f"ID: {user_id}\n"
    )

    await callback.message.edit_text(text=profile_text,
                                     reply_markup=kb.back_to_settings()
                                     )
    


@router.callback_query(F.data == "open_help")
async def show_help(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="В разработке",
                                     reply_markup=kb.back_to_settings()
                                     )



@router.callback_query(F.data == "go_to_main")
async def back_main(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Добро пожаловать в финбот!",
                                     reply_markup=kb.main
                                     )

@router.callback_query(F.data == "go_to_settings")
async def back_settings(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="⚙️Настройки:",
                                     reply_markup=await kb.settings_buttons()
                                     )