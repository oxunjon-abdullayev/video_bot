from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards.inline.my_inline_button import inline_genereal_button, update_inline_check
from loader import db, dp
from states.state import EditProductState


@dp.message_handler(Text(equals='⬅️ cancel'), state="*")
async def get_cancel(message: types.Message, state: FSMContext):
    await message.answer_photo(
        photo="https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg",
        reply_markup=inline_genereal_button())
    await message.answer(text=f"orqaga",
                         reply_markup=ReplyKeyboardRemove())
    await state.finish()


@dp.message_handler(state=EditProductState.id)
async def edit_product(message: types.Message, state: FSMContext):
    try:
        product_id = int(message.text)
        product = db.get_product(id=product_id)

        if product:
            async with state.proxy() as data:
                data['id'] = message.text
            await message.answer_video(video=product[3],
                                       caption=f"📹   <b>Videoning nomi :</b> {product[1]}\n"
                                               f"📹   <b>Videoning ta'rifi :</b> {product[2]}\n",
                                       reply_markup=update_inline_check())
        else:
            await message.answer("Bu id raqamga tegishli video topilmadi . ")


    except:
        await message.answer("Id raqam bo'lsin")


@dp.callback_query_handler(state=EditProductState)
async def check_call_data(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "edit_title":
        await callback.message.answer("Video nomini  yangilang ")
        await EditProductState.title.set()

    elif callback.data == "edit_description":

        await callback.message.answer("Video ta'rifini yangilang ")
        await EditProductState.description.set()



    elif callback.data == "edit_photo":
        await callback.message.answer("Video yuklang ")
        await EditProductState.video.set()

    elif callback.data == 'back_to_start':
        await callback.message.answer_photo(
            photo='https://www.geirangerfjord.no/upload/images/2018_general/film-and-vid.jpg  ',
            reply_markup=inline_genereal_button())
        await state.finish()


@dp.message_handler(state=EditProductState.title)
async def edit_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
        update_id = data["id"]

    db.update_product_title(id=update_id, title=data['title'])
    product_id = int(data['id'])
    product = db.get_product(id=product_id)
    await message.answer_video(video=product[3],
                               caption=f"📹   <b>Videoning nomi :</b> {product[1]}\n"
                                       f"📹   <b>Videoning ta'rifi : </b>{product[2]}\n"
                               ,
                               reply_markup=update_inline_check())


@dp.message_handler(state=EditProductState.description)
async def edit_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        update_id = data["id"]

    db.update_product_description(id=update_id, description=data['description'])
    product_id = int(data['id'])
    product = db.get_product(id=product_id)
    await message.answer_video(video=product[3],
                               caption=f"📹   <b>Videoning nomi :</b> {product[1]}\n"
                                       f"📹   <b>Videoning ta'rifi :</b> {product[2]}\n",
                               reply_markup=update_inline_check())


@dp.message_handler(lambda message: not message.video, state=EditProductState.video)
async def check_video(message: types.Message):
    await message.answer("Bu video formatida emas")


@dp.message_handler(state=EditProductState.video, content_types=['video'])
async def add_video(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['video'] = message.video.file_id

        db.update_product_video(id=data['id'],
                                video=data['video'])
        product = db.get_product(data['id'])
        await message.answer_video(video=product[3],
                                   caption=f"📹   <b>Videoning nomi :</b> {product[1]}\n"
                                           f"📹   <b>Videoning ta'rifi : </b> {product[2]}\n",
                                   reply_markup=update_inline_check())
