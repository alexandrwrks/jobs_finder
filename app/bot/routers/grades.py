from aiogram import F, Router
from aiogram.types import CallbackQuery

from app.bot.keyboards.grades import change_grades_v1
from app.services.users_service import users_service

router = Router()



@router.callback_query(F.data == "menu:add_grades")
async def menu_grades(callback: CallbackQuery):
    user = await users_service.get_user(callback.from_user.id)
    await callback.message.answer(
        text="Выберите грэйды которые вам подходят:",
        reply_markup=change_grades_v1(user)
    )

@router.callback_query(F.data.startswith("grade_"))
async def change_grades(callback: CallbackQuery):
    level = callback.data.split("_")[1]

    user = await users_service.change_grade(
        telegram_id=callback.from_user.id,
        level=level
    )

    await callback.message.edit_reply_markup(
        reply_markup=change_grades_v1(user)
    )

    await callback.answer()