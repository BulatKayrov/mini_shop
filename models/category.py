from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from models import Base

if TYPE_CHECKING:
    from .product import Product


class Category(Base):
    __tablename__ = 'category'

    name: Mapped[str]

    products: Mapped[list['Product']] = relationship(back_populates='category')

    def __repr__(self):
        return f"<Category(name='{self.name}')>"
