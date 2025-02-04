import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import settings
from bot.handlers import handler


logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=settings.TOKEN_BOT)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(handler.router)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
