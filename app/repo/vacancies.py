from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Vacancies


class VacanciesRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_vacancies(self, vacancy_id: str, title: str) -> None:
        await self.session.execute(
            insert(Vacancies)
            .values(id=vacancy_id, title=title)
        )

    async def find_vacancies(self, vacancies_id: str) -> Vacancies | None:
        result = await self.session.execute(
            select(Vacancies)
            .where(Vacancies.id == vacancies_id)
        )

        return result.scalar_one_or_none()