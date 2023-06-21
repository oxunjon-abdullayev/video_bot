from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.matsarenno_inline_button import inline_genereal_button
from loader import dp, db
from states.matsarenno_state import DeleteProductState

@dp.message_handler(Text(equals='cancel'), state="*")
async def check_cancel(message:types.Message,state:FSMContext):
    await message.answer_photo(photo = 'https://previews.agefotostock.com/previewimage/medibigoff/0116e67d8e7bf305f948d3e3665fb2a8/esy-048015155.jpg',
                         reply_markup=inline_genereal_button())
    await state.finish()

@dp.message_handler(state=DeleteProductState.id)
async def delete_product(message: types.Message, state:FSMContext):
        try:
                product_id= int(message.text)
                product = db.get_product(product_id)
                if product:
                        db.delete_product(product_id)
                        await message.answer("<b>Bu mahsulot o'chirildi</b>\n\n\n\n")

                        await message.answer_photo(photo='https://previews.agefotostock.com/previewimage/medibigoff/0116e67d8e7bf305f948d3e3665fb2a8/esy-048015155.jpg'
                                             ,reply_markup=inline_genereal_button())
                        await state.finish()
                else:
                        await message.answer("Bu 🆔 ga tegishli mahsulot topilmadi ")
        except:
                await message.answer("Id raqam bo'lsin")



