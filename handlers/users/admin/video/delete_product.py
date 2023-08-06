from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.my_inline_button import inline_genereal_button
from loader import dp, db
from states.state import DeleteProductState


@dp.message_handler(Text(equals='⬅️  ortga qaytish'), state="*")
async def check_cancel(message: types.Message, state: FSMContext):
    await message.answer_photo(
        photo='https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg',
        reply_markup=inline_genereal_button())
    await message.answer(text=f"orqaga",
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(state=DeleteProductState.id)
async def delete_product(message: types.Message, state: FSMContext):
    try:
        product_id = int(message.text)
        product = db.get_product(product_id)
        if product:
            db.delete_product(product_id)
            await message.answer("<b>Bu video o'chirildi</b>\n\n\n\n")

            await message.answer_photo(
                photo='https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg'
                , reply_markup=inline_genereal_button())
            await state.finish()
        else:
            await message.answer("Bu 🆔 ga tegishli video topilmadi ")
    except:
        await message.answer("Id raqam bo'lsin")
