from aiogram.dispatcher.filters.state import StatesGroup, State


class FeedbackState(StatesGroup):
    feedback = State()


class AddProductState(StatesGroup):
    title = State()
    description = State()
    price = State()
    photo = State()


class EditProductState(StatesGroup):
    id = State()
    title = State()
    description = State()
    price = State()
    photo = State()


class DeleteProductState(StatesGroup):
    id = State()


class AllProductState(StatesGroup):
    id = State()

