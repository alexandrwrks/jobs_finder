from app.db.config import new_session
from app.repo.query import RequestRepository


class RequestService:
    async def add_query(self, telegram_id: int, query: str) -> None:
        try:
            async with new_session() as session:
                request_repo = RequestRepository(session)

                request = await request_repo.get(telegram_id)
                if request is None:
                    await request_repo.create_request(telegram_id, query)

                    print("Успешное добавление нового запроса")
                elif request is not None:
                    await request_repo.update(telegram_id, query)

                    print("Успешное обновление запроса")

                await session.commit()

        except Exception as e:
            print(e)
            await session.rollback()


request_services = RequestService()