

import psutil
from aiogram import F, Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()

# Ограничение доступа: впишите свой ID цифрами (без кавычек), например: 123456789
# Если хотите, чтобы статус сервера могли смотреть абсолютно все — оставьте None
ADMIN_ID = None  

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
    # Чтобы код не падал, временно отправляем текст. Сюда можно вставить реальный file_id фото
    await message.answer('Здесь должна быть отправка фото. Передайте рабочий file_id в метод answer_photo.')


@router.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


# --- НОВАЯ КОМАНДА СТАТУСА СЕРВЕРА ---
@router.message(Command("status"))
async def check_status(message: Message):
    # Проверка на админа (если ADMIN_ID заполнен)
    if ADMIN_ID and message.from_user.id != ADMIN_ID:
        return

    # Собираем метрики без интервала ожидания
    cpu_usage = psutil.cpu_percent(interval=None)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    battery = psutil.sensors_battery()	
   

    # Переводим байты в Гигабайты и округляем
    ram_used = round(ram.used / (1024 ** 3), 2)
    ram_total = round(ram.total / (1024 ** 3), 2)
    disk_free = round(disk.free / (1024 ** 3), 2)
    disk_total = round(disk.total / (1024 ** 3), 2)

    # Формируем текст ответа с HTML-тегами Aiogram
    status_text = (
        f"📊 СТАТУС СЕРВЕРА:\n\n"
        f"🤖 Процессор: {cpu_usage}%\n"
        f"🧠 ОЗУ: {ram_used} ГБ / {ram_total} ГБ ({ram.percent}%)\n"
        f"💾 Свободно на диске: {disk_free} ГБ из {disk_total} ГБ\n"
        f"🔋 Батарея: {round(battery.percent)}%,\n ⏳Осталось заряда на: {(battery.secsleft // 60)//60} часов\n🔌 Подключен к сети: {battery.power_plugged} "
    )

    await message.answer(status_text)

