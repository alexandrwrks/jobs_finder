from aiogram.utils.keyboard import InlineKeyboardBuilder


def back_to_start():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="🔙 Вернуться в главное меню", callback_data="menu:start")
    return keyboard.as_markup()