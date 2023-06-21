from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.inline.matsarenno_inline_button import inline_genereal_button
from loader import dp, db
from states.matsarenno_state import AddProductState


@dp.message_handler(state=AddProductState.title)
async def add_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text

    await message.answer("Mahsulotning ta'rifini kiriting ")
    await AddProductState.next()


@dp.message_handler(state=AddProductState.description)
async def add_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    await AddProductState.next()
    await message.answer("Mahsulotning narxini kiriting ")


@dp.message_handler(state=AddProductState.price)
async def add_number(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['price'] = float(message.text)
            if data['price']:
                await message.answer(text='Mahsulotning rasmini kiriting ')
                await AddProductState.next()
            else:
                await message.answer("Mahsulotning narxini kiritishda xatolik bor")
        except:
                await message.answer(text="Xato ")


@dp.message_handler(lambda message: not message.photo, state=AddProductState.photo)
async def check_photo(message: types.Message):
    await message.answer("Bu rasm formatida emas")


@dp.message_handler(state=AddProductState.photo, content_types=['photo'])
async def add_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id


    await message.answer_photo(photo=data['photo'],
                               caption=f"<b><i> Mahsulot nomi : {data['title']}\n"
                         f"Mahsulotning ta'rifi :  {data['description']}\n"
                         f"Mahsulotning narxi  : {data['price']} </i></b>")
    db.add_product(title=data['title'],
                   description=data['description'],
                   price=data['price'],
                   photo=data['photo'])
    await message.answer(text="Ma'lumotingiz saqlandi")
    await message.answer_photo(photo='https://previews.agefotostock.com/previewimage/medibigoff/0116e67d8e7bf305f948d3e3665fb2a8/esy-048015155.jpg',
                         reply_markup=inline_genereal_button())
    await state.finish()



