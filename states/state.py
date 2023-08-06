from aiogram.dispatcher.filters.state import StatesGroup, State


class AddProductState(StatesGroup):
    title = State()
    description = State()
    video = State()
    category_id = State()


class EditProductState(StatesGroup):
    id = State()
    title = State()
    description = State()
    video = State()
    category_id = State()


class DeleteProductState(StatesGroup):
    id = State()


class AllProductState(StatesGroup):
    id = State()


class AddCategoryState(StatesGroup):
    title = State()


class DeleteCategoryState(StatesGroup):
    id = State()


class AllCategoryState(StatesGroup):
    id = State()


class ShowCategoryState(StatesGroup):
    id = State()
