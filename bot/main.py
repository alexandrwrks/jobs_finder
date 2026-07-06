import asyncio

from aiogram import Dispatcher

from bot.routers import routers
from bot_settings import bot


async def main() -> None:
    dp = Dispatcher()

    print("Including routers...")

    dp.include_routers(routers)

    print("Starting bot...")

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopping bot...")