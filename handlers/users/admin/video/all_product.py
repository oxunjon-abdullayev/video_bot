from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.my_default_button import cancel_product_button
from keyboards.inline.my_inline_button import inline_genereal_button, inline_back_category
from loader import dp, db
from states.state import AllProductState, ShowCategoryState


@dp.callback_query_handler(state=AllProductState.id)
async def all_user(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.data
    user = db.get_product(id=user_id)
    if callback.data != "back":
        await callback.bot.send_video(chat_id=callback.message.chat.id, video=user[3],
                                      caption=f"📽️   <b>Video nomi  :</b> {user[1]}\n\n"
                                              f"📽️  <b>  Video ta'rifi  :</b> {user[2]}\n\n</b>",
                                      reply_markup=cancel_product_button())
        await state.finish()
    elif callback.data == "back":
        await callback.message.answer_photo(
            photo="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
            reply_markup=inline_genereal_button())
        await state.finish()


@dp.callback_query_handler(state=ShowCategoryState.id)
async def all_user(callback: types.CallbackQuery, state: FSMContext):
    video_id = callback.data
    video = db.get_product(id=video_id)

    await callback.bot.send_video(chat_id=callback.message.chat.id, video=video[3],
                                  caption=f"📽️   <b>Video nomi  :  </b> {video[1]}\n\n"
                                          f"📽️   <b> Video ta'rifi  : </b> {video[2]}\n\n",
                                  reply_markup=inline_back_category())
    await state.finish()
