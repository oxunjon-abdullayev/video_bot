from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def order_default_button():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = KeyboardButton("🚚   Yetkazib  berish")
    btn2 = KeyboardButton("🚶  Borib olish")
    btn3 = KeyboardButton('⬅️ Ortga')
    rkm.add(btn, btn2, btn3)
    return rkm







