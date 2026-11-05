from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import Vacancies


class VacanciesRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_vacancies(self, url: str, title: str) -> None:
        await self.session.execute(
            insert(Vacancies)
            .values(url=url, title=title)
        )

    async def find_vacancies(self, url: str) -> Vacancies | None:
        result = await self.session.execute(
            select(Vacancies)
            .where(Vacancies.id == url)
        )

        return result.scalar_one_or_none()