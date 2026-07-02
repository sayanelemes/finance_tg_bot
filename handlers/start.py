import psutil

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()


ADMIN_id = None  # Замените на ID администратора, если нужно ограничить доступ к команде /status

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! твой ID: {message.from_user.id} Имя: {message.from_user.first_name}')


@router.message(Command('help'))    # ждет команду /help
async def get_help(message: Message):
    await message.answer('Это команда /help')





@router.message(Command("status"))
async def check_status(message: Message):
    if ADMIN_id and message.from_user.id != ADMIN_id:
        return


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





    await message.answer(status_text)

