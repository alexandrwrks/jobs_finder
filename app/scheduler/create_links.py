import asyncio
from typing import List

import httpx
from pydantic import BaseModel

from app.db.config import new_session
from app.db.models import Grades
from app.links.create_links import create_query_url
from app.parsers.job_links import get_job_links
from app.repo.query import RequestRepository
from app.repo.user import UsersRepository


class UserDataLinks(BaseModel):
    telegram_id: int
    levels: List[Grades]
    query: str


async def get_users():
    async with new_session() as session:
        user_repo = UsersRepository(session)
        request_repo = RequestRepository(session)

        users = await user_repo.get_users()

        async with httpx.AsyncClient() as client:
            for user in users:
                user_request = await request_repo.get(telegram_id=user.telegram_id)

                query = ""
                if user_request is not None:
                    query = user_request.query

                # Передаём данные в функцию которая собирает ссылки: объект Users и query-параметр
                await send_vacancy(
                    UserDataLinks(
                        telegram_id=user.telegram_id,
                        levels=user.grades,
                        query=query
                    ),
                    client=client
                )


async def send_vacancy(user_data: UserDataLinks, client: httpx.AsyncClient):
    params = create_query_url(user_data.levels, user_data.query)
    print("Успешно получили параметры")

    print("Работа с получением вакансий с url")
    await get_job_links(params, user_data.telegram_id, client)

if __name__ == "__main__":
    asyncio.run(get_users())
