import asyncio
import os
import logging



from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers.start import router


load_dotenv()  # импорт токена с .env
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        import sys
        sys.exit(0)
