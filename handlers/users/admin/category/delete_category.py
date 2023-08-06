from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.my_inline_button import inline_category_button
from loader import dp, db2, db
from states.state import DeleteCategoryState


@dp.message_handler(Text(equals='⬅️ Orqaga qaytish'), state="*")
async def check_cancel(message: types.Message, state: FSMContext):
    await message.answer_photo(
        photo='https://t4.ftcdn.net/jpg/00/81/38/59/360_F_81385977_wNaDMtgrIj5uU5QEQLcC9UNzkJc57xbu.jpg',
        reply_markup=inline_category_button())

    await message.answer(text=f"orqaga qaytish",
                                  reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(state=DeleteCategoryState.id)
async def delete_category(message: types.Message, state: FSMContext):
    try:
        category_id = int(message.text)
        category = db2.get_category(category_id=category_id)
        if category:
            db2.delete_category(message.text)

            db.delete_products_by_category(category_id=message.text)

            await message.answer("<b>Bu kategoriya o'chirildi</b>\n\n\n\n",
                reply_markup=ReplyKeyboardRemove())
            await message.answer_photo(
                photo='https://t4.ftcdn.net/jpg/00/81/38/59/360_F_81385977_wNaDMtgrIj5uU5QEQLcC9UNzkJc57xbu.jpg',
                reply_markup=inline_category_button()
            )
            
            await state.finish()

        else:
            await message.answer("<b>Bu id ga tegishli categoriya topilmadi !</b>")
    except:
        await message.answer("Id raqam bo'lsin")
