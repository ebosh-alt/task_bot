from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def create_keyboard(name_buttons: list | dict, *sizes: int) -> types.InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    for name_button in name_buttons:
        if type(name_buttons[name_button]) is tuple:
            if len(name_buttons[name_button]) == 2:
                keyboard.button(
                    text=name_button, url=name_buttons[name_button][0], callback_data=name_buttons[name_button][1]
                )
            else:
                if "http" in name_buttons[name_button]:
                    keyboard.button(
                        text=name_button, url=name_button
                    )
                keyboard.button(
                    text=name_button, callback_data=name_button
                )

        else:

            if "http" in str(name_buttons[name_button]):
                keyboard.button(
                    text=name_button, url=name_buttons[name_button]
                )
            else:
                keyboard.button(
                    text=name_button, callback_data=name_buttons[name_button]
                )
    if len(sizes) == 0:
        sizes = (1,)
    keyboard.adjust(*sizes)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=True)


def create_reply_keyboard(name_buttons: list, one_time_keyboard: bool = False, *sizes) -> types.ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    for name_button in name_buttons:
        if name_button is not tuple:
            keyboard.button(
                text=name_button
            )
        else:
            keyboard.button(
                text=name_button,

            )
    if len(sizes) == 0:
        sizes = (1,)
    keyboard.adjust(*sizes)
    return keyboard.as_markup(resize_keyboard=True, one_time_keyboard=one_time_keyboard)

main_menu = create_reply_keyboard(["Назад"])



