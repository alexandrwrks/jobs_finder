from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Vacancies(Base):
    __tablename__ = 'vacancies'

    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    title: Mapped[str]


class Users(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(primary_key=True)


class UsersRequest(Base):
    __tablename__ = 'users_requests'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(ForeignKey("users.telegram_id"))
    request: Mapped[str]