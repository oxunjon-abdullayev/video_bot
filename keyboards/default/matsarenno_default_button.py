from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def cancel_default_button() :
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="cancel")
    rkm.add(button)
    return rkm


def update_cancel() :
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="⬅️ cancel")
    rkm.add(button)
    return rkm










