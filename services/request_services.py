from db.config import new_session
from repo.request import RequestRepository


class RequestService:
    async def add_query(self, telegram_id: int, request: str) -> None:
        try:
            async with new_session() as session:
                request_repo = RequestRepository(session)

                request_ = await request_repo.get(telegram_id)
                if request_ is None:
                    await request_repo.create_request(telegram_id, request)

                    print("Успешное добавление нового запроса")
                elif request_ is not None:
                    await request_repo.update(telegram_id, request)

                    print("Успешное обновление запроса")

                await session.commit()

        except Exception as e:
            print(e)
            await session.rollback()


request_services = RequestService()