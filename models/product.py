from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base

if TYPE_CHECKING:
    from .category import Category


class Product(Base):
    __tablename__ = 'product'

    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str | None]
    image: Mapped[str | None]
    quantity_for_cart: Mapped[int] = mapped_column(default=0)

    category_pk: Mapped[int] = mapped_column(ForeignKey(column='category.pk', ondelete='CASCADE'))
    category: Mapped['Category'] = relationship(back_populates='products')

    def __repr__(self):
        return f'<Product {self.name}>'
