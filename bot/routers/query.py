from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.fsm.schemas import FSM
from parsers.job_links import get_job_links, save_query

router = Router()

@router.callback_query(F.data == "add_query")
async def add_query(callback: CallbackQuery, state: FSMContext):

    await state.set_state(FSM.query)

    await callback.message.answer(
        text="Напишите нужные вам запрос для вакансии",
    )

@router.message(FSM.query)
async def add_query(message: Message, state: FSMContext):
    await state.update_data(query=message.text)

    await message.answer(
        text="Сохранили ваш запрос, в скором времени начнём поиск вакансий"
    )

    data = await state.get_data()

    url = await save_query(data["query"])
    await get_job_links(url)



