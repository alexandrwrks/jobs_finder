from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.db.models import Users


def change_grades_v1(user: Users):
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="✅ Junior" if "junior" in user.grades else "⬜ Junior",
        callback_data="grade_junior",
    )

    keyboard.button(
        text="✅ Mid" if "mid" in user.grades else "⬜ Mid",
        callback_data="grade_mid",
    )

    keyboard.button(
        text="✅ Senior" if "senior" in user.grades else "⬜ Senior",
        callback_data="grade_senior",
    )

    keyboard.button(
        text="✅ Lead" if "lead" in user.grades else "⬜ Lead",
        callback_data="grade_lead",
    )

    return keyboard.adjust(1).as_markup()