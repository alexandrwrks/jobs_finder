from sqlalchemy import select, insert, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import UsersRequest


class RequestRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, telegram_id: int) -> UsersRequest | None:
        result = await self.session.execute(
            select(UsersRequest)
            .where(UsersRequest.telegram_id == telegram_id)
        )

        return result.scalar_one_or_none()

    async def create_request(self, telegram_id: int, request: str) -> None:
        await self.session.execute(
            insert(UsersRequest)
            .values(
                telegram_id=telegram_id,
                request=request,
            )
        )

    async def delete(self, telegram_id: int) -> None:
        await self.session.execute(
            delete(UsersRequest)
            .where(UsersRequest.telegram_id == telegram_id)
        )

    async def update(self, telegram_id: int, request: str) -> None:
        await self.session.execute(
            update(UsersRequest)
            .values(request=request)
            .where(UsersRequest.telegram_id == telegram_id)
        )