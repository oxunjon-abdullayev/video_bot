from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db, db2, dp, bot
from states.state import ShowCategoryState


def inline_main_button():
    rkm = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton("👨‍🏫      Video darsliklar", callback_data="video_lesson")
    btn2 = InlineKeyboardButton("📘       Biz haqimizda", callback_data="about_us")
    rkm.add(btn, btn2)
    return rkm


def inline_genereal_button():
    rkm = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton("✅ Video qo'shish", callback_data='add_product')
    btn2 = InlineKeyboardButton("✅ Hamma videolar", callback_data='all_product')
    btn3 = InlineKeyboardButton("✅ Video o'chirish", callback_data='delete_product')
    btn4 = InlineKeyboardButton("✅ Video almashtirish", callback_data='update_product')
    btn5 = InlineKeyboardButton("✅ Asosiy menuga qaytish ", callback_data='back_menu')

    rkm.add(btn, btn2, btn3, btn4, btn5)
    return rkm


def inline_category_button():
    rkm = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton("✅ Categoryiya qo'shish", callback_data='add_category')
    btn2 = InlineKeyboardButton("✅ Categoryiya o'chirish", callback_data='delete_category')
    btn3 = InlineKeyboardButton("✅ Asosiy menuga qaytish ", callback_data='back_menu')
    rkm.add(btn, btn2, btn3)
    return rkm


def update_inline_check():
    ikm = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton("Video nomi", callback_data="edit_title")
    button1 = InlineKeyboardButton("Video ta'rifi", callback_data="edit_description")
    button3 = InlineKeyboardButton("Video ", callback_data="edit_photo")
    button4 = InlineKeyboardButton("⬅️  Orqaga qaytish", callback_data="back_to_start")
    ikm.add(button, button1, button3, button4)
    return ikm


def delete_product_button():
    ikm = InlineKeyboardMarkup()
    products = db.all_product()
    if not products:
        button = InlineKeyboardButton(text="Sizda videolar yo'q", callback_data="no_products")
        ikm.add(button)
    else:
        for i in products:
            button = InlineKeyboardButton(text=f"ID: {i[0]}  Videoning nomi: {i[1]}", callback_data=str(i[0]))
            ikm.add(button)
    return ikm


def delete_category_button():
    ikm = InlineKeyboardMarkup()
    products = db2.all_category()
    if not products:
        button = InlineKeyboardButton(text="Sizda categoriyalar yo'q", callback_data="no_products")
        ikm.add(button)
    else:
        for i in products:
            button = InlineKeyboardButton(text=f"ID : {i[0]}                      categoriyaning nomi : {i[1]}",
                                          callback_data=f"{i[0]}")
            ikm.add(button)
    return ikm


def asosiy_menu():
    rkm = InlineKeyboardMarkup()
    btn = InlineKeyboardButton('⏪      Asosiy menu', callback_data="main_menu")
    return rkm.add(btn)


def show_products():
    ikm = InlineKeyboardMarkup(row_width=2)
    for i in db.all_product():
        button = InlineKeyboardButton(text=f"{i[1]}", callback_data=f"{i[0]}")
        ikm.add(button)
    button1 = InlineKeyboardButton(text=" ⬅️  Orqaga qaytish",
                                   callback_data="back")
    ikm.add(button1)
    return ikm


def inline_back_category_button():
    ikm = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text=" ⬅️  Orqaga qaytish", callback_data="back_to_inline_category_button")
    ikm.add(button1)
    return ikm


def inline_back_main_button():
    ikm = InlineKeyboardMarkup(row_width=2)
    button1 = InlineKeyboardButton(text=" ⬅️  Orqaga qaytish", callback_data="back_to_inline_main_button")
    ikm.add(button1)
    return ikm


def show_category():
    ikm = InlineKeyboardMarkup(row_width=2)
    categories = db2.all_category()

    if categories:
        for category in categories:
            button = InlineKeyboardButton(text=category[1], callback_data=category[0])
            ikm.add(button)

        button1 = InlineKeyboardButton(text=" ⬅️  Orqaga qaytish", callback_data="back_to_inline_main_button")
        ikm.add(button1)

    return ikm


def inline_back_category():
    rkm = InlineKeyboardMarkup(row_width=1)
    button1 = InlineKeyboardButton(text=" ⬅️  Orqaga qaytish", callback_data="back_in_category")
    rkm.add(button1)
    return rkm


def show_category_in_video():
    ikm = InlineKeyboardMarkup()
    categories = db2.all_category()

    for i in categories:
        button2 = InlineKeyboardButton(text=f"{i[1]}", callback_data=f"{i[0]}")
        ikm.add(button2)
    return ikm


@dp.callback_query_handler(lambda query: query.data.isdigit())
async def handle_category_selection(query: types.CallbackQuery, state: FSMContext):
    category_id = int(query.data)

    videos = db.get_category_id_videos(category_id)

    if videos:
        video_ikm = InlineKeyboardMarkup(row_width=2)

        for video in videos:
            button = InlineKeyboardButton(text=video[1], callback_data=f"{video[0]}")
            video_ikm.add(button)
        button1 = InlineKeyboardButton(text=" ⬅️  Orqaga qaytish", callback_data="back_in_category")
        video_ikm.add(button1)

        await bot.send_message(query.from_user.id, f"<b><em> 💁‍♀️   Bu categoriyaga tegishli videolar jamlanmasi </em></b> ", reply_markup=video_ikm)
        await ShowCategoryState.id.set()
    else:
        await bot.send_message(query.from_user.id, "<b><em>❓   Ushbu turkumda hech qanday video topilmadi.</em></b>",
                               reply_markup=inline_back_category_button())
