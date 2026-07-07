from enum import StrEnum
from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Grades(StrEnum):
    junior = "junior"
    mid = "mid"
    senior = "senior"
    lead = "lead"


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(unique=True, index=True)
    grades: Mapped[List[Grades]] = mapped_column(ARRAY(String(30)))


class UsersRequest(Base):
    __tablename__ = 'users_requests'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(ForeignKey("users.telegram_id"), unique=True)
    query: Mapped[str] = mapped_column(String)


class Vacancies(Base):
    __tablename__ = 'vacancies'

    id: Mapped[str] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)


