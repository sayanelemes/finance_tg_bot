from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! твой ID: {message.from_user.id} Имя: {message.from_user.first_name}')


@router.message(Command('help'))    # ждет команду /help
async def get_help(message: Message):
    await message.answer('Это команда /help')


@router.message(F.text == 'Как дела')  # ждет сообщение 'Как дела'
async def how_are_you(message: Message):
    await message.answer('OK!')


@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='')


@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')