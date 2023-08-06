from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.my_default_button import update_cancel, cancel_product_button, cancel_category_button, \
    main_default_button
from keyboards.inline.my_inline_button import inline_category_button, inline_genereal_button, delete_product_button, \
    show_products, delete_category_button, show_category, inline_main_button, inline_back_main_button
from loader import dp, db2
from states.state import AddProductState, AllProductState, DeleteProductState, EditProductState, AddCategoryState, \
    DeleteCategoryState


@dp.message_handler(Text(equals="🟧   Categoriyalar qo'shish"))
async def category_func(message: types.Message):
    await message.answer(text='Asosiy menu',
                         reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://t4.ftcdn.net/jpg/00/81/38/59/360_F_81385977_wNaDMtgrIj5uU5QEQLcC9UNzkJc57xbu.jpg",
        reply_markup=inline_category_button())


@dp.message_handler(Text(equals="📽️   Videolar"))
async def category_func(message: types.Message):
    await message.answer(text='Asosiy menu',
                         reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
        reply_markup=inline_genereal_button())


@dp.message_handler(Text(equals='⬅️Orqaga qaytish'), state="*")
async def check_cancel(message: types.Message, state: FSMContext):
    await message.answer(text='Asosiy menu',
                         reply_markup=main_default_button())

    await state.finish()


@dp.message_handler(Text(equals='⬅️  ortga qaytish'), state="*")
async def check_cancel(message: types.Message, state: FSMContext):
    await message.answer_photo(
        photo='https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg',
        reply_markup=inline_genereal_button())
    await message.answer(text=f"orqaga qaytish",
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.callback_query_handler()
async def check_inline_button(callback: types.CallbackQuery):
    if callback.data == "add_product":
        await callback.message.answer(text="<b>Video nomini kiriting </b>",
                                      reply_markup=cancel_product_button())

        await AddProductState.title.set()

    elif callback.data == "delete_product":
        await callback.message.answer(text=f"<b>▶️ Qaysi 🆔 ga tegishli videoni o'chirmoqchisiz ? </b>",
                                      reply_markup=delete_product_button())
        await callback.message.answer(text=f"<b>O'chirmoqchi bo'lgan videolaringiz  🆔"
                                           f"raqamini kiriting </b>",
                                      reply_markup=cancel_product_button())
        await DeleteProductState.id.set()


    elif callback.data == "all_product":
        await callback.message.answer(text="<b> Hamma videolar</b>",
                                      reply_markup=show_products())
        await AllProductState.id.set()

    elif callback.data == "update_product":
        await callback.message.answer(text='Videolarni tahrirlash',
                                      reply_markup=delete_product_button())
        await callback.message.answer(text="<b>Qaysi id ga tegishli videoni yangilamoqchisiz ? </b> ",
                                      reply_markup=update_cancel())
        await EditProductState.id.set()

    elif callback.data == "add_category":
        await callback.message.answer(text="<b>Categoriya nomini kiriting </b>",
                                      reply_markup=ReplyKeyboardRemove())

        await AddCategoryState.title.set()

    elif callback.data == "delete_category":
        category = db2.all_category()
        if not category:
            await callback.message.answer(text="Sizda categoriyalar yo'q",
                                          reply_markup=delete_category_button())
        else:
            await callback.message.answer(text=f"<b>▶️ Qaysi 🆔 ga tegishli categoriyani o'chirmoqchisiz ? </b>",
                                          reply_markup=delete_category_button())
            await callback.message.answer(text=f"<b>O'chirmoqchi bo'lgan categoriyangizni  🆔"
                                               f"raqamini kiriting </b>",
                                          reply_markup=cancel_category_button())

        await DeleteCategoryState.id.set()

    elif callback.data == "back_menu":
        await callback.message.answer(text="orqaga qaytish",
                                      reply_markup=main_default_button())

    elif callback.data == "about_us":
        await callback.message.answer_photo(
            photo="https://thumbs.dreamstime.com/b/online-education-social-distancing-protect-covid-viruses-happy-english-teacher-recording-vlog-looking-gesturing-234689124.jpg",
            caption="<b>Assalomu alaykum!</b> Bizning onlayn darslar platformamizga xush kelibsiz. Bizning maqsadimiz, sizga o'rganish "
                    "jarayonida qulaylik va samarali yordam berishdir. Biz murabbiylar jamoasidan tashkil topganmiz va xususiy "
                    "o'qituvchilar bilan hamkorlik qilamiz.Bizning darslarimizga online ravishda kirish imkoniyatingiz bor. Siz o'zingizga qulay vaqt tanlaysiz va darslarga istalgan joydan kirishingiz mumkin. Bizning platformamiz o'zgartirishga ochiq, bu saytdan o'zgarishlarni kuzatib boramiz va o'qituvchilarimizning yangi materiallarini tez-tez qo'shamiz. "

                    "Bizning o'quvchilarimizning fikrlariga katta e'tibor beramiz va sizning talablarizni qondiramiz.",
            reply_markup=inline_back_main_button())

    elif callback.data == "video_lesson":
        await callback.message.answer(text='categoriyalar',
                                      reply_markup=ReplyKeyboardRemove())
        await callback.message.answer_photo(
            photo="https://thumbs.dreamstime.com/b/online-education-social-distancing-protect-covid-viruses-happy-english-teacher-recording-vlog-looking-gesturing-234689124.jpg",
            reply_markup=show_category())

    elif callback.data == "back_in_category":
        await callback.message.answer_photo(
            'https://thumbs.dreamstime.com/b/online-education-social-distancing-protect-covid-viruses-happy-english-teacher-recording-vlog-looking-gesturing-234689124.jpg',
            reply_markup=show_category())

    elif callback.data == "back_to_inline_main_button":
        await callback.message.answer_photo(
            'https://thumbs.dreamstime.com/b/online-education-social-distancing-protect-covid-viruses-happy-english-teacher-recording-vlog-looking-gesturing-234689124.jpg',
            reply_markup=inline_main_button())

    elif callback.data == "back_to_inline_category_button":
        await callback.message.answer_photo(
            'https://thumbs.dreamstime.com/b/online-education-social-distancing-protect-covid-viruses-happy-english-teacher-recording-vlog-looking-gesturing-234689124.jpg',
            reply_markup=show_category())

    elif callback.data == "no_category_back":
        await callback.message.answer(text="Cagegoriyalar",
                                      reply_markup=inline_genereal_button())

        # await ShowCategoryState.id.set()
