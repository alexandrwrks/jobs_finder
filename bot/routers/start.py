from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.keyboards.start import start_keyboard

router = Router()

WELCOME_TEXT = (
    f"Добро пожаловать!\n\n"
    f"Данный бот помогает находить вакансии нужные Вам\n"
    f"От Вас только нужно написать нужное слово/а и поиск начнёт работать"
)

@router.message(Command('start'))
async def start(message: Message) -> None:
    await message.answer(
        text=WELCOME_TEXT,
        reply_markup=start_keyboard()
    )