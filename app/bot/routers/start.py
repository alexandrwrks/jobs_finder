from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from app.bot.keyboards.query import start_keyboard
from app.services.users_service import users_service

router = Router()

WELCOME_TEXT = (
    f"Добро пожаловать!\n\n"
    f"Данный бот помогает находить вакансии нужные Вам\n"
    f"От Вас только нужно написать нужное слово/а и поиск начнёт работать"
)

@router.message(Command('start'))
async def start(message: Message) -> None:
    await users_service.add_user(message.from_user.id)

    await message.answer(
        text=WELCOME_TEXT,
        reply_markup=start_keyboard()
    )

@router.callback_query(F.data == "menu:start")
async def menu(message: Message) -> None:
    await message.answer(
        text=WELCOME_TEXT,
        reply_markup=start_keyboard()
    )