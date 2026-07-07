from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keyboard():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Добавить query параметр", callback_data="menu:add_query")
    keyboard.button(text="Добавить грэйды", callback_data="menu:add_grades")

    return keyboard.adjust().as_markup()
