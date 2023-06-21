from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.matsarenno_inline_button import asosiy_menu
from loader import dp
from states.matsarenno_state import FeedbackState


@dp.message_handler(state=FeedbackState.feedback)
async def feedback_user(message:types.Message,state:FSMContext):
    await message.answer(text="<em><b>️🔸🔸🔸   Xurmatli mijoz fikrlaringiz qabul qilindi   🔸🔸🔸</b></em>",
                         reply_markup=asosiy_menu())
    await state.finish()