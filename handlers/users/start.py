from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.default.my_default_button import main_default_button
from keyboards.inline.my_inline_button import inline_main_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer(text="Admin xush kelibsiz !")
        await message.answer(text='Asosiy menu',
                             reply_markup=main_default_button())

    else:

        await message.answer(f"Salom, {message.from_user.full_name} bizning botimizga xush kelibsiz!")
        await message.answer_photo(
            photo="https://www.modernenglishteacher.com/media/38646/sponsored1.jpg?width=500&height=299.2847563701386",
            reply_markup=inline_main_button())


