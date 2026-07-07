from typing import List

from app.db.config import new_session
from app.db.models import Users
from app.repo.user import UsersRepository
from app.schemas.grades import GradesSchema


class UsersService:
    async def add_user(self, telegram_id: int) -> None:
        try:
            async with new_session() as session:
                users_repo = UsersRepository(session)

                user = await users_repo.get_user_by_id(telegram_id)

                if user is None:
                    await users_repo.create_user(telegram_id)
                    await session.commit()
                    print("Успешное добавление пользователя")


        except Exception as e:
            print(e)
            await session.rollback()


    async def get_user(self, telegram_id: int) -> Users:
        try:
            async with new_session() as session:
                users_repo = UsersRepository(session)

                user = await users_repo.get_user_by_id(telegram_id)
                if user is None:
                    raise

                return user

        except Exception as e:
            print(e)
            await session.rollback()
            raise

    async def change_grade(self, telegram_id: int, level: int) -> Users:
        try:
            async with new_session() as session:
                users_repo = UsersRepository(session)

                user = await users_repo.get_user_by_id(telegram_id)
                if user is None:
                    raise

                grades: list = user.grades.copy()
                if level in grades:
                    grades.remove(level)
                else:
                    grades.append(level)

                user = await users_repo.change_grade(telegram_id, grades)

                await session.commit()
                
                return user
        except Exception as e:
            print(e)
            await session.rollback()
            raise

users_service = UsersService()