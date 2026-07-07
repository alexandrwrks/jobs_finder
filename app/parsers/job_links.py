import asyncio

import httpx
from bs4 import BeautifulSoup

from app.bot.send_job_info import send_job_info_to_telegram
from app.services.vacancies_service import vacancies_service
from app.utils.my_decorators import timelog

main_link = "https://talanto.work/"

@timelog
async def get_job_links(params: dict, telegram_id: int, client: httpx.AsyncClient) -> None:
    response = await client.get(url=main_link, params=params)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    articles = soup.find_all("article")
    lens = len(articles)
    print(lens)
    for article in articles:
        href = article.find("a")["href"]
        vacancy_id = href.split("/")[-1]
        exists_vacancy = await vacancies_service.check_vacancy(vacancy_id)
        if exists_vacancy is None:
            await send_job_info_to_telegram(f"https://talanto.work{href}", telegram_id, client)

    print("End...")

if __name__ == "__main__":
    asyncio.run(get_job_links())