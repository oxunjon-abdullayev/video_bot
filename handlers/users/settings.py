from aiogram import types

from keyboards.default.matsarenno_default_button import order_default_button
from keyboards.inline.matsarenno_inline_button import inline_main_button, asosiy_menu
from loader import dp
from states.matsarenno_state import FeedbackState


@dp.callback_query_handler()
async def about_us(callback:types.CallbackQuery):

    if callback.data == "main_menu":
        await callback.message.answer_photo(photo="https://previews.123rf.com/images/grafner/grafner1505/grafner150500042/40558742-fast-food-meal-on-white-background.jpg",
                                      reply_markup=inline_main_button())

    elif callback.data == "about_us":
        await callback.message.answer_photo(photo='https://img.freepik.com/free-vector/fast-food-background-linear-graphic-snack-collection-junk-food-engraved-top-view-illustration-vector-illustration_91128-1536.jpg',
                                            caption="Biz O‘zbekiston bozorida yaqin  yillardan beri faoliyat yuritamiz!\n\nMazali va to‘yimli taomlar, qulay narxlar, tez yetkazib"
                                  " berish\n\nxizmatidan mamnun mijozlar yana va yana bizni tanlamoqda.\n\n"
                                  "Qaynoqqina va mazali fast-food mahsulotlarimizni\n\nalbatta "
                                 "tatib ko'rishingizni tavsiya etamiz\n\n\n<b><em>Yetkazib berish xizmati:  +998781500030</em></b>",
                                            reply_markup=asosiy_menu())

    elif callback.data == "our_address":
        await callback.bot.send_location(chat_id=callback.message.chat.id,
                                         latitude=38.850038,
                                         longitude=65.796602,reply_markup=asosiy_menu())

    elif callback.data == 'comment':
        await callback.message.answer(text="✍️ Fikrlaringizni yozib qoldiring ")
        await FeedbackState.feedback.set()


    elif callback.data == "order":
        await callback.message.answer(text='Buyurtma turini tanlang ',
                                      reply_markup=order_default_button())
