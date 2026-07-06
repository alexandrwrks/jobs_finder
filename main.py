import asyncio

from parsers.job_links import get_job_links

if __name__ == '__main__':
    print("Старт программы")
    asyncio.run(get_job_links())



