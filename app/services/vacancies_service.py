from app.db.config import new_session
from app.repo.vacancies import VacanciesRepository


class VacanciesService:
    async def check_vacancy(self, vacancy_id: str):
        try:
            async with new_session() as session:
                vacancy_repo = VacanciesRepository(session)

                exist_vacancy = await vacancy_repo.find_vacancies(vacancy_id)

                return exist_vacancy

        except Exception:
            await session.rollback()
            raise

    async def add_vacancy(self, vacancy_id: str, title: str):
        try:
            async with new_session() as session:
                vacancy_repo = VacanciesRepository(session)

                await vacancy_repo.add_vacancies(vacancy_id, title)
                await session.commit()

        except Exception:
            await session.rollback()
            raise

vacancies_service = VacanciesService()