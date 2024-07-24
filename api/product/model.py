from fastapi import HTTPException
from sqlalchemy import select, Result

from models import session_scope, Product


class ProductModel:

    @classmethod
    async def find_all(cls):
        async with session_scope() as session:
            stmt = select(Product).order_by(Product.pk)
            result: Result = await session.execute(stmt)
            return result.scalars().all()

    @classmethod
    async def find_by_category_pk(cls, category_pk):
        async with session_scope() as session:
            stmt = select(Product).where(Product.category_pk == category_pk)
            result: Result = await session.execute(stmt)
            return result.scalars().all()

    @classmethod
    async def create(cls, **data):
        async with session_scope() as session:
            product = Product(**data)
            session.add(product)
            await session.commit()
            return product

    @classmethod
    async def update(cls, pk, **data):
        async with session_scope() as session:
            stmt = select(Product).where(Product.pk == pk)
            result: Result = await session.execute(stmt)
            product = result.scalars().first()
            if product:
                for key, value in data.items():
                    setattr(product, key, value)
                await session.commit()
                return product

            raise HTTPException(status_code=404, detail="Product not found")

    @classmethod
    async def delete(cls, pk):
        async with session_scope() as session:
            stmt = select(Product).where(Product.pk == pk)
            result: Result = await session.execute(stmt)
            product = result.scalars().first()
            if product:
                session.delete(product)
                await session.commit()
                return product

            raise HTTPException(status_code=404, detail="Product not found")
