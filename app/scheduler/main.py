import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def my_sync_job():
    print("Старт работы...")
    await asyncio.sleep(1)
    print("Конец работы...")


async def main():
    scheduler = AsyncIOScheduler()

    scheduler.add_job(my_sync_job, 'interval', seconds=5)

    scheduler.start()

    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Работа завершена.")