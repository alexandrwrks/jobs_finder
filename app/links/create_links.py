from typing import List

import httpx

from app.db.models import Grades
from app.parsers.job_links import get_job_links

main_link = "https://talanto.work/"

MAIN_PARAMETERS = {
    "search_in": ["title", "skills"],
    "sort": "newest",
    "period": "month",
}



def create_query_url(levels: List[Grades], query: str, offset: int = 0):

    return {
        **MAIN_PARAMETERS,
        "offset": offset,
        "levels": levels,
        "q": query
    }



async def take_vacancies_from_url(params: dict, client: httpx.AsyncClient) -> str:
    try:
        response = await client.get(main_link, params=params)
        response.raise_for_status()

        print(response.url)
        await get_job_links(str(response.url), client)
        return str(response.url)

    except Exception as e:
        print(e)
        raise
