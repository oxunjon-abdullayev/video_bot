from aiogram import types

from loader import dp

@dp.callback_query_handler()
async def about_us(callback:types.CallbackQuery):
    if callback.data == "about_us":
        await callback.message.answer_photo(photo='',caption="Biz O‘zbekiston bozorida yaqin  yillardan beri faoliyat yuritamiz! Mazali va to‘yimli taomlar, qulay narxlar, tez yetkazib"
                                  " berish xizmatidan mamnun mijozlar yana va yana bizni tanlamoqda."
                                  "Qaynoqqina va mazali fast-food mahsulotlarimizni albatta tatib ko'rishingizni tavsiya etamiz")