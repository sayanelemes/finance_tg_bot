from aiogram.fsm.state import StatesGroup, State

class AddExpense(StatesGroup):
    category = State()
    amount = State()