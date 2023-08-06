from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_default_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True, row_width=1)
    btn = KeyboardButton(text='📽️   Videolar')
    btn2 = KeyboardButton(text="🟧   Categoriyalar qo'shish")
    rkm.add(btn, btn2)
    return rkm


def cancel_product_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="⬅️  ortga qaytish")
    rkm.add(button)
    return rkm



def cancel_category_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text="⬅️ Orqaga qaytish")
    rkm.add(button)
    return rkm


def cancel_user_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = KeyboardButton(text="⬅️ Orqaga qaytish")
    rkm.add(button)
    return rkm


def update_cancel():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True,
                              one_time_keyboard=True)
    button = KeyboardButton(text="⬅️ cancel")
    rkm.add(button)
    return rkm
