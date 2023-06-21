from aiogram import types

from aiogram.types import ReplyKeyboardRemove

from keyboards.default.matsarenno_default_button import cancel_default_button, update_cancel
from keyboards.inline.matsarenno_inline_button import delete_product_button, show_products
from loader import dp
from states.matsarenno_state import AddProductState, AllProductState, DeleteProductState, EditProductState


@dp.callback_query_handler()
async def check_inline_button(callback:types.CallbackQuery):
    if callback.data=="add_product":
        await callback.message.answer(text="Mahsulotlar ro'yxatiga qo'shish",
                                      reply_markup=ReplyKeyboardRemove())
        await AddProductState.title.set()

    elif callback.data == "delete_product":
        await callback.message.answer(text=f"<b>▶️ Qaysi 🆔 ga tegishli mahsulotni o'chirmoqchisiz ? </b>",
                                      reply_markup=delete_product_button())
        await callback.message.answer(text=f"<b>O'chirmoqchi bo'lgan mahsulotingizning  🆔"
                                           f"raqamini kiriting </b>",
                                      reply_markup=cancel_default_button())
        await DeleteProductState.id.set()


    elif callback.data =="all_product":
        await callback.message.answer(text="Hamma mahsulotlar",
                                      reply_markup=show_products())
        await AllProductState.id.set()

    elif callback.data == "update_product":
        await callback.message.answer(text='Mahsulotlarni tahrirlash',
                                      reply_markup=delete_product_button())
        await callback.message.answer(text="<b>Qaysi id ga tegishli mahsulotni yangilamoqchisiz ? </b> ",
                                      reply_markup=update_cancel())
        await EditProductState.id.set()


