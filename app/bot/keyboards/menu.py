from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_main_menu():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Изменить параметр поиск", callback_data="change_request")

    return keyboard.as_markup()