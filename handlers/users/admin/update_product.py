
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from keyboards.inline.matsarenno_inline_button import update_inline_check, inline_genereal_button
from loader import db, dp
from states.matsarenno_state import EditProductState


@dp.message_handler(Text(equals='⬅️ cancel'), state="*")
async def get_cancel(message:types.Message,state:FSMContext):
    await message.answer_photo(photo="https://previews.agefotostock.com/previewimage/medibigoff/0116e67d8e7bf305f948d3e3665fb2a8/esy-048015155.jpg  ",
                         reply_markup=inline_genereal_button())
    await state.finish()


@dp.message_handler(state=EditProductState.id)
async def edit_product(message: types.Message, state: FSMContext):
    try:
        product_id = int(message.text)
        product = db.get_product(id=product_id)

        if product:
            async with state.proxy() as data:
                data['id'] = message.text
            await message.answer_photo(photo=product[4],
                                       caption=f"Mahsulotning nomi : {product[1]}\n"
                                               f"Mahsulotning ta'rifi : {product[2]}\n"
                                               f"Mahsulotning narxi : {product[3]}\n"
                                               ,
                                       reply_markup=update_inline_check())
        else:
            await message.answer("Bu id raqamga tegishli mahsulot topilmadi . ")


    except:
        await message.answer("Id raqam bo'lsin")


@dp.callback_query_handler(state=EditProductState)
async def check_call_data(callback:types.CallbackQuery, state:FSMContext):
    if callback.data == "edit_title":
        await callback.message.answer("Mahsulot nomini  yangilang ")
        await EditProductState.title.set()

    elif callback.data == "edit_description":

        await callback.message.answer("Mahsulot ta'rifini yangilang ")
        await EditProductState.description.set()

    elif callback.data == "edit_price":

        await callback.message.answer("Mahsulot narxini yangilang ")
        await EditProductState.price.set()


    elif callback.data == "edit_photo":

        await callback.message.answer("Rasmni yuklang ")
        await EditProductState.photo.set()

    elif callback.data == 'back_to_start':
        await callback.message.answer_photo(photo='https://previews.agefotostock.com/previewimage/medibigoff/0116e67d8e7bf305f948d3e3665fb2a8/esy-048015155.jpg', reply_markup=inline_genereal_button())
        await state.finish()

@dp.message_handler(state=EditProductState.title)
async def edit_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
        update_id = data["id"]

    db.update_product_title(id=update_id,title=data['title'])
    product_id = int(data['id'])
    product = db.get_product(id=product_id)
    await message.answer_photo(photo=product[4],
                               caption=f"Mahsulotning nomi : {product[1]}\n"
                                       f"Mahsulotning ta'rifi : {product[2]}\n"
                                       f"Mahsulotning narxi : {product[3]}\n",
                               reply_markup=update_inline_check())

@dp.message_handler(state=EditProductState.description)
async def edit_age(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        update_id = data["id"]

    db.update_product_description(id=update_id, description=data['description'])
    product_id = int(data['id'])
    product = db.get_product(id=product_id)
    await message.answer_photo(photo=product[4],
                               caption=f"Mahsulotning nomi : {product[1]}\n"
                                       f"Mahsulotning ta'rifi : {product[2]}\n"
                                       f"Mahsulotning narxi : {product[3]}\n",
                               reply_markup=update_inline_check())


@dp.message_handler(state=EditProductState.price)
async def edit_phone_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['price'] = message.text
            if data['price']:

                db.update_product_price(id=data['id'],
                                 price=data['price'])
                product = db.get_product(data['id'])
                await message.answer_photo(photo=product[4],
                                       caption=f"Mahsulotning nomi : {product[1]}\n"
                                               f"Mahsulotning ta'rifi : {product[2]}\n"
                                               f"Mahsulotning narxi : {product[3]}\n"
                                             ,
                                       reply_markup=update_inline_check())

            else:
                    await message.answer("Narxni kiritishda xatolik bor!")

        except:
                await message.answer(text="Narxni kiritishda xatolik bor")


@dp.message_handler(lambda message: not message.photo, state=EditProductState.photo)
async def check_photo(message: types.Message):
    await message.answer("Bu rasm formatida emas")


@dp.message_handler(state=EditProductState.photo, content_types=['photo'])
async def add_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id

        db.update_product_photo(id=data['id'],
                             photo=data['photo'])
        product = db.get_product(data['id'])
        await message.answer_photo(photo=product[4],
                                   caption=f"Mahsulotning nomi : {product[1]}\n"
                                           f"Mahsulotning ta'rifi : {product[2]}\n"
                                           f"Mahsulotning narxi : {product[3]}\n",
                                   reply_markup=update_inline_check())
