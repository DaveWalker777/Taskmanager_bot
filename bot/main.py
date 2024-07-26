import logging
import asyncio
from aiogram import Bot, Dispatcher
from config import API_TOKEN
from handlers import register_handlers

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def on_startup(dispatcher: Dispatcher):
    logging.info("Bot is starting...")

async def on_shutdown(dispatcher: Dispatcher):
    logging.info("Bot is shutting down...")

async def main():
    register_handlers(dp)
    await dp.start_polling(bot, on_startup=on_startup, on_shutdown=on_shutdown)

if __name__ == '__main__':
    asyncio.run(main())
