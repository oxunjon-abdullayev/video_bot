from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.matsarenno_inline_button import inline_main_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name} bizning botimizga xush kelibsiz!")
    await message.answer_photo(photo="https://previews.123rf.com/images/grafner/grafner1505/grafner150500042/40558742-fast-food-meal-on-white-background.jpg",
                               reply_markup=inline_main_button())
