from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.matsarenno_default_button import cancel_default_button
from keyboards.inline.matsarenno_inline_button import inline_genereal_button
from loader import db, dp
from states.matsarenno_state import AllProductState



@dp.callback_query_handler(state=AllProductState.id)
async def all_user(callback:types.CallbackQuery, state: FSMContext):
        user_id = callback.data
        user = db.get_product(id=user_id)
        if callback.data != "back":
            await callback.message.answer_photo(photo=user[4],
           caption=f"✅<b>Mahsulotning nomi  : {user[1]}\n\n"
            f"✅ Mahsulotning ta'rifi  : {user[2]}\n\n"
            f"✅ Mahsulotning  narxi : {user[3]}\n\n</b>",
                                      reply_markup=cancel_default_button())
            await state.finish()
        elif callback.data == "back":
            await callback.message.answer_photo(photo="https://previews.agefotostock.com/previewimage/medibigoff/0116e67d8e7bf305f948d3e3665fb2a8/esy-048015155.jpg",
                                          reply_markup=inline_genereal_button())
            await state.finish()