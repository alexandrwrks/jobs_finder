from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app.bot.fsm.schemas import FSM
from app.bot.keyboards.menu import get_main_menu
from app.parsers.job_links import get_job_links
from app.services.request_services import request_services

router = Router()


@router.callback_query(F.data == "menu:add_query")
async def add_query(callback: CallbackQuery, state: FSMContext):

    await state.set_state(FSM.query)

    await callback.message.answer(
        text="Напишите нужные вам запрос для вакансии",
    )

@router.message(FSM.query)
async def add_query(message: Message, state: FSMContext):
    await state.update_data(query=message.text)

    data = await state.get_data()
    await request_services.add_query(message.from_user.id, data["query"])

    await message.answer(
        text="Сохранили ваш запрос, в скором времени начнём поиск вакансий"
    )




