from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keyboard():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Добавить query параметр", callback_data="add_query")

    return keyboard.as_markup()