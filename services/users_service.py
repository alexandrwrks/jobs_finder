from db.config import new_session
from repo.user import UsersRepository


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



users_service = UsersService()