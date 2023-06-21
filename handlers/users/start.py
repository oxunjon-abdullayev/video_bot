from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.matsarenno_inline_button import inline_main_button, inline_genereal_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    if message.from_user.id == 5895762331:
        await message.answer(text="Admin xush kelibsiz !")
        await message.answer_photo(photo='https://previews.agefotostock.com/previewimage/medibigoff/0116e67d8e7bf305f948d3e3665fb2a8/esy-048015155.jpg',
                             reply_markup=inline_genereal_button())

    else:

        await message.answer(f"Salom, {message.from_user.full_name} bizning botimizga xush kelibsiz!")
        await message.answer_photo(photo="https://previews.123rf.com/images/grafner/grafner1505/grafner150500042/40558742-fast-food-meal-on-white-background.jpg",
                                   reply_markup=inline_main_button())


