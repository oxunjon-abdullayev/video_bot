from aiogram.dispatcher.filters.state import StatesGroup, State


class FeedbackState(StatesGroup):
    feedback = State()
