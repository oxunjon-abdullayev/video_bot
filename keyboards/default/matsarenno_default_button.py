from aiogram.types import InlineKeyboardMarkup,  InlineKeyboardButton


def inline_main_button():
    rkm = InlineKeyboardMarkup(row_width=2)
    btn = InlineKeyboardButton("🛒 Buyurtma berish",callback_data="w")
    btn2 = InlineKeyboardButton("🛍 Buyurtmalarim",callback_data="e")
    btn3 = InlineKeyboardButton("📘 Biz haqimizda",callback_data="about_us")
    btn4 = InlineKeyboardButton("✍️Fikr bildirish",callback_data="ew")
    btn5 = InlineKeyboardButton("📍 Bizning manzil",callback_data="dskds")
    rkm.add(btn, btn2, btn3, btn4,btn5)
    return rkm