from database.models import async_session
from database.models import User, Category, Expense
from sqlalchemy import select, func


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

    
async def get_categories():
    async with async_session() as session:
        result = await session.scalars(select(Category))
        return result.all()
    

async def add_expense(user_id: int, category_id: int, amount: float):
    async with async_session() as session:
        session.add(Expense(user_id=user_id, category_id=category_id, amount=amount))
        await session.commit()



async def get_user_stats(user_tg_id: int):
    async with async_session() as session:
        stmt = (
            select(Category.name, func.sum(Expense.amount))
            .join(Category, Expense.category_id == Category.id)
            .where(Expense.user_id == user_tg_id)
            .group_by(Category.name)
        )
        
        result = await session.execute(stmt)
        rows = result.all()
        
        if not rows:
            return "У вас пока нет расходов."
        
        text = "📊 Статистика расходов:\n\n"
        for category_name, total in rows:
            text += f"▪️ {category_name}: {total} тг.\n"
            
        return text