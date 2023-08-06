from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.my_inline_button import inline_category_button
from loader import dp, db2
from states.state import AddCategoryState


@dp.message_handler(state=AddCategoryState.title)
async def add_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
        db2.add_category(title=data['title'])

        await message.answer_photo(photo="https://t4.ftcdn.net/jpg/00/81/38/59/360_F_81385977_wNaDMtgrIj5uU5QEQLcC9UNzkJc57xbu.jpg",
                                   reply_markup=inline_category_button())

        await state.finish()
