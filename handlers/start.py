import handlers.keyboards as kb
import database.requests as rq
from database.requests import add_expense


from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from handlers.expense import AddExpense

router = Router()


class Reg(StatesGroup):
    name = State()
    number = State()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer("Добро пожаловать в финбот!",reply_markup=kb.main)




@router.callback_query(F.data == "settings")
async def show_settings(callback: CallbackQuery):
    await callback.answer("⚙️Настройки")
    await callback.message.edit_text("⚙️Настройки:", reply_markup=await kb.settings_buttons())

@router.callback_query(F.data == "open_profile")
async def show_profile(callback: CallbackQuery):
    await callback.answer()
    
    user_name = callback.from_user.first_name
    user_id = callback.from_user.id

    profile_text = (
        f"👤Ваш Профиль:\n"
        f"Имя: {user_name}\n"
        f"ID: {user_id}\n"
    )

    await callback.message.edit_text(text=profile_text,
                                     reply_markup=kb.back_to_settings()
                                     )
    


@router.callback_query(F.data == "open_help")
async def show_help(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="В разработке",
                                     reply_markup=kb.back_to_settings()
                                     )



@router.callback_query(F.data == "go_to_main")
async def back_main(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Добро пожаловать в финбот!",
                                     reply_markup=kb.main
                                     )

@router.callback_query(F.data == "go_to_settings")
async def back_settings(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="⚙️Настройки:",
                                     reply_markup=await kb.settings_buttons()
                                     )
    


@router.callback_query(F.data == "add_expense")
async def expenses(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text("📝 Добавить расход", reply_markup=await kb.categories_keyboard())




@router.callback_query(F.data.startswith("category_"))
async def category_selected(callback: CallbackQuery, state: FSMContext):

    category_id = int(callback.data.split("_")[1])
    

    await state.update_data(chosen_category_id=category_id)
    

    await state.set_state(AddExpense.amount)
    

    await callback.message.edit_text("Отлично! Теперь введите сумму расхода (только цифры):")
    await callback.answer()

@router.message(AddExpense.amount)
async def process_amount(message: Message, state: FSMContext):
    try:
       
        amount = float(message.text)
    except ValueError:
      
        await message.answer("Пожалуйста, введите сумму только цифрами (например, 150 или 75.50):")
        return
    

    user_data = await state.get_data()
    category_id = user_data.get("chosen_category_id")
    

    await add_expense(user_id=message.from_user.id, category_id=category_id, amount=amount)
    

    await state.clear()
    

    await message.answer(f"✅ Расход успешно добавлен! Сумма: {amount} тенге.", reply_markup=await kb.categories_keyboard())