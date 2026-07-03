import psutil, os

from dotenv import load_dotenv
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from handlers.keyboards import admin_keyboard

router = Router()

load_dotenv()
env_id = os.getenv('ADMIN_ID', '').strip()
ADMIN_id = int(env_id) if env_id.isdigit() else None

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! твой ID: {message.from_user.id} Имя: {message.from_user.first_name}')


@router.message(Command('commands'))  # Ловит команду /commands
async def get_help(message: Message):
    if ADMIN_id and message.from_user.id == ADMIN_id:
        await message.answer(
            "Вот доступные команды и меню:", 
            reply_markup=admin_keyboard()
        )




@router.message(F.text == "📊 СТАТУС СЕРВЕРА")
async def check_status(message: Message):
    if ADMIN_id and message.from_user.id == ADMIN_id:
        cpu_usage = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        battery = psutil.sensors_battery()

    
        ram_used = round(ram.used / (1024 ** 3), 2)
        ram_total = round(ram.total / (1024 ** 3), 2)
        disk_free = round(disk.free / (1024 ** 3), 2)
        disk_total = round(disk.total / (1024 ** 3), 2)

    
        status_text = (
            f"📊 СТАТУС СЕРВЕРА:\n\n"
            f"🤖 Процессор: {cpu_usage}%\n"
            f"🧠 ОЗУ: {ram_used} ГБ / {ram_total} ГБ ({ram.percent}%)\n"
            f"💾 Свободно на диске: {disk_free} ГБ из {disk_total} ГБ\n"
        )
        if battery:
            status_text += f"🔋 Батарея: {round(battery.percent)}%"
            if battery.power_plugged:
                status_text += f"\n⏳Осталось заряда на: ∞\n🔌Подключен к сети: Да"
            else:
                status_text += f"\n⏳Осталось заряда на: {(battery.secsleft // 60)//60} часов\n🔌 Подключен к сети: Нет"
        else:
            status_text += "🔋 Батарея: Не обнаружена\n"




    else:
        status_text = "Нет доступа"
        
    await message.answer(status_text)


