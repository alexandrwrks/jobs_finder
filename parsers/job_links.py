import asyncio

import httpx
from bs4 import BeautifulSoup

from bot.send_job_info import send_job_info_to_telegram
from utils.my_decorators import timelog


async def save_query(query: str) -> str:
    # Отдаём ссылку с нужным query параметром

    url = (
        f"https://talanto.work/?sort=newest&period=month&"
        f"offset=1&search_in=title&levels=junior&levels=mid&"
        f"work_formats=remote&work_formats=hybrid&q={query}"
    )

    return url

@timelog
async def get_job_links(url: str, telegram_id: int) -> None:
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(url=url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("article")
        lens = len(articles)
        print(lens)
        for article in articles:
            href = article.find("a")["href"]
            await send_job_info_to_telegram(f"https://talanto.work{href}", telegram_id, client)

        print("End...")

if __name__ == "__main__":
    asyncio.run(get_job_links())