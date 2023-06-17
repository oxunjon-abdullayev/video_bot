from aiogram.types import InlineKeyboardMarkup,  InlineKeyboardButton


def inline_main_button():
    rkm = InlineKeyboardMarkup(row_width=2)
    btn = InlineKeyboardButton("🛒 Buyurtma berish",callback_data="order")
    btn2 = InlineKeyboardButton("🛍 Buyurtmalarim",callback_data="my_order")
    btn3 = InlineKeyboardButton("📘 Biz haqimizda",callback_data="about_us")
    btn4 = InlineKeyboardButton("✍️Fikr bildirish",callback_data="comment")
    btn5 = InlineKeyboardButton("📍 Bizning manzil",callback_data="our_address")
    rkm.add(btn, btn2, btn3, btn4,btn5)
    return rkm



def asosiy_menu():
    rkm = InlineKeyboardMarkup()
    btn = InlineKeyboardButton('⏪      Asosiy menu',callback_data="main_menu")
    return rkm.add(btn)