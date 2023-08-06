from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.my_inline_button import inline_genereal_button, show_category_in_video
from loader import dp, db, db2
from states.state import AddProductState


@dp.message_handler(Text(equals='⬅️  ortga qaytish'), state="*")
async def check_cancel(message: types.Message, state: FSMContext):
    await message.answer_photo(
        photo='https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg',
        reply_markup=inline_genereal_button())
    await message.answer(text=f"orqaga",
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(state=AddProductState.title)
async def add_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text

    await message.answer("<b>Videoning ta'rifini kiriting </b>")
    await AddProductState.next()


@dp.message_handler(state=AddProductState.description)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    await AddProductState.next()
    await message.answer("<b>Videoni kiriting </b>")


@dp.message_handler(lambda message: not message.video, state=AddProductState.video)
async def check_non_video(message: types.Message):
    await message.answer("<b>Siz kiritgan narsa mp4 formatida emas !\n\nIltimos qayta kiriting</b>")


@dp.message_handler(content_types=['photo'], state=AddProductState.video)
async def check_photo(message: types.Message):
    await message.answer("<b>Siz kiritgan narsa mp4 formatida emas !\nIltimos qayta kiriting</b>")


@dp.message_handler(content_types=['document', 'audio', 'voice'], state=AddProductState.video)
async def check_non_video(message: types.Message):
    await message.answer("<b>Siz kiritgan narsa mp4 formatida emas !\nIltimos qayta kiriting</b>")


@dp.message_handler(content_types=['video'], state=AddProductState.video)
async def add_video(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['video'] = message.video.file_id
        categories = db2.all_category()
        if not categories:
            await message.answer(
                text="<b><em>Sizda categoriya yo'q categoriyalar bo'imidan categoriya qo'shing  </em></b>")
        else:
            await message.answer("<b>Qaysi kategoriyaga kiritmoqchisiz?</b>",
                                 reply_markup=show_category_in_video())

            await AddProductState.next()


@dp.callback_query_handler(state=AddProductState.category_id)
async def add_video(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['category_id'] = callback.data
        db.add_product(title=data['title'],
                       description=data['description'],
                       video=data['video'],
                       category_id=data['category_id'])
        await state.finish()
        await callback.message.answer(text="<b><em>Bu video muvaffaqiyatli ravishda qabul qilindi !</em></b>")

        await callback.message.answer_photo(
            photo='https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg',
            reply_markup=inline_genereal_button())
