from sqlalchemy import select, Result, delete

from models import Category, session_scope


class CategoryModel:

    @classmethod
    async def find_all(cls):
        async with session_scope() as session:
            stmt = select(Category)
            result: Result = await session.execute(stmt)
            return result.scalars().all()

    @classmethod
    async def create(cls, **kwargs):
        async with session_scope() as session:
            category = Category(**kwargs)
            session.add(category)
            await session.commit()
            return category

    @classmethod
    async def update(cls, pk: int, **kwargs):
        async with session_scope() as session:
            stmt = select(Category).where(Category.pk == pk)
            result: Result = await session.execute(stmt)
            category = result.scalars().first()

            for key, value in kwargs.items():
                setattr(category, key, value)

            await session.commit()
            return category

    @classmethod
    async def delete(cls, pk: int):
        async with session_scope() as session:
            stmt = delete(Category).where(Category.pk == pk)
            await session.execute(stmt)
            await session.commit()
            return None
