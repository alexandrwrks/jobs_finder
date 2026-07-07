from aiogram.fsm.state import State, StatesGroup


class FSM(StatesGroup):
    query = State()