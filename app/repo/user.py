from typing import List

from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Users


class UsersRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, telegram_id: int) -> Users | None:
        result = await self.session.execute(
            select(Users)
            .where(Users.telegram_id == telegram_id)
        )

        return result.scalar_one_or_none()

    async def create_user(self, telegram_id: int):
        await self.session.execute(
            insert(Users)
            .values(
                telegram_id=telegram_id,
                grades=[]
            )
        )

    async def change_grade(self, telegram_id: int, grades: list) -> Users:
        result = await self.session.execute(
            update(Users)
            .values(grades=grades)
            .where(Users.telegram_id == telegram_id)
            .returning(Users)
        )

        return result.scalar_one()


    async def get_users(self) -> List[Users]:
        result = await self.session.execute(select(Users))

        return list(result.scalars().all())