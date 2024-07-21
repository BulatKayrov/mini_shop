from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = 'user'

    email: Mapped[str]
    password: Mapped[str]
    image: Mapped[str]
    is_admin: Mapped[bool | None] = mapped_column(default=False)
    is_active: Mapped[bool | None] = mapped_column(default=False)

    def __repr__(self):
        return f'<User {self.email}>'
