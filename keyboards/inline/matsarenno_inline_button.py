from aiogram.types import InlineKeyboardMarkup,  InlineKeyboardButton

from loader import db


def inline_main_button():
    rkm = InlineKeyboardMarkup(row_width=2)
    btn = InlineKeyboardButton("🛒 Buyurtma berish",callback_data="order")
    btn2 = InlineKeyboardButton("🛍 Bizning mahsulotlar",callback_data="my_order")
    btn3 = InlineKeyboardButton("📘 Biz haqimizda",callback_data="about_us")
    btn4 = InlineKeyboardButton("✍️Fikr bildirish",callback_data="comment")
    btn5 = InlineKeyboardButton("📍 Bizning manzil",callback_data="our_address")
    rkm.add(btn, btn2, btn3, btn4,btn5)
    return rkm


def inline_genereal_button():
    rkm = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton("✅ Mahsulot qo'shish", callback_data='add_product')
    btn2 = InlineKeyboardButton("✅ Hamma mahsulotlar", callback_data='all_product')
    btn3 = InlineKeyboardButton("✅ Mahsulot o'chirish", callback_data='delete_product')
    btn4 = InlineKeyboardButton("✅ Mahsulot almashtirish", callback_data='update_product')
    rkm.add(btn, btn2, btn3, btn4)
    return rkm


def update_inline_check():
    ikm = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Mahsulot nomi",callback_data="edit_title")
    button1 = InlineKeyboardButton("Mahsulot ta'rifi",callback_data="edit_description")
    button2 = InlineKeyboardButton("Mahsulot narxi ",callback_data="edit_price")
    button3 = InlineKeyboardButton("Mahsulot rasmi",callback_data="edit_photo")
    button4 = InlineKeyboardButton("Back to home",callback_data="back_to_start")
    ikm.add(button,button1,button2,button3,button4)
    return ikm

def delete_product_button():
    ikm = InlineKeyboardMarkup()
    for i in db.all_product():
        button = InlineKeyboardButton(text=f"ID : {i[0]}                      Mahsulotning nomi : {i[1]}",callback_data=f"{i[0]}")
        ikm.add(button)
    return ikm


def asosiy_menu():
    rkm = InlineKeyboardMarkup()
    btn = InlineKeyboardButton('⏪      Asosiy menu',callback_data="main_menu")
    return rkm.add(btn)


def show_products():
    ikm = InlineKeyboardMarkup(row_width=2)
    for i in db.all_product():
        button = InlineKeyboardButton(text=f"{i[1]}",callback_data=f"{i[0]}")
        ikm.add(button)
    button1= InlineKeyboardButton(text="🛒 Back to home",
                                  callback_data="back")
    ikm.add(button1)
    return ikm


