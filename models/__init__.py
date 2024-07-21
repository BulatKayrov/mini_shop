__all__ = [
    'Base',
    'User',
    'session_scope',
    'Category',
    'Product',
    'Order',
    'OrderProduct'
]

from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import settings
from .base import Base
from .category import Category
from .order import Order
from .order_product import OrderProduct
from .product import Product
from .user import User

engine = create_async_engine(url=settings.SQLALCHEMY_DATABASE_URI)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False, autocommit=False, autoflush=False)


@asynccontextmanager
async def session_scope():
    async with async_session() as session:
        yield session
