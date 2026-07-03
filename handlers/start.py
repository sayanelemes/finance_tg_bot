import handlers.keyboards as kb


from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! {message.from_user.first_name}',
        reply_markup=kb.main
    )
#@router.message(Command('commands'))  # Ловит команду /commands
#async def get_help(message: Message):
#    await message.answer(
#        "Вот доступные команды и меню:"
#        )




@router.callback_query(F.data == 'settings')
async def status(callback: CallbackQuery):
    await callback.answer('Настройки')
    await callback.message.edit_text('Настройки:', reply_markup=await kb.inline_test())